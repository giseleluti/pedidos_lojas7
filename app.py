from flask import Flask, jsonify, request, redirect
from flasgger import Swagger, swag_from
import logging
import json
from src.model.Pedidos import Pedidos

from src.repository.Database import init_database
from src.service.Pedidos_service import PedidoService

app = Flask(__name__)

# Configurações do Swagger
app.config['SWAGGER'] = {
    'title': 'API Pedidos_lojas7 com base nos produtos da fakestore',
    'uiversion': 3,
    'ui': 'swagger-ui'
}
swagger = Swagger(app)

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Carrega o schema do arquivo JSON
with open('src/model/data/pedidos_schema.json', 'r') as f:
    pedido_schema = json.load(f)


@app.route('/pedidos/criar', methods=['POST'])
@swag_from({
    'summary': 'Cria um novo pedido',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': pedido_schema.get("Pedido", {}),  # Usa o schema carregado
        }
    ],
    'responses': {
        '201': {
            'description': 'Pedido criado com sucesso',
            'schema': pedido_schema.get('Pedido', {})  # Usa o schema carregado
        },
        '500': {
            'description': 'Erro ao criar pedido'
        }
    }
})
def criar_pedido():
    """Rota para criar um novo pedido."""
    try:
        logger.info('Criando um novo pedido.')
        body = request.get_json()
        pedido = Pedidos(**body)
        return PedidoService.criar_pedido(pedido)
    except Exception as e:
        logger.error(f'Erro ao criar pedido: {e}')
        return jsonify({'error': str(e)}), 500


@app.route('/pedidos/<int:id_pedido>', methods=['GET'])
@swag_from({
    'summary': 'Busca um pedido por ID',
    'parameters': [
        {
            'name': 'id_pedido',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do pedido'
        }
    ],
    'responses': {
        '200': {
            'description': 'Pedido encontrado',
            'schema': pedido_schema.get('Pedido', {})  # Usa o schema carregado
        },
        '404': {
            'description': 'Pedido não encontrado'
        }
    }
})
def obter_pedido_rota(id_pedido: int):
    """Rota para buscar um pedido por ID."""
    try:
        logger.info(f'Buscando pedido com ID: {id_pedido}')
        return PedidoService.obter_pedido(id_pedido)
    except Exception as e:
        logger.error(f'Erro ao buscar pedido com ID {id_pedido}: {e}')
        return jsonify({'error': str(e)}), 500


@app.route('/pedidos/<int:id_pedido>', methods=['PUT'])
@swag_from({
    'summary': 'Atualiza um pedido por ID',
    'parameters': [
        {
            'name': 'id_pedido',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do pedido'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': pedido_schema.get('Pedido', {})  # Usa o schema carregado
        }
    ],
    'responses': {
        '200': {
            'description': 'Pedido atualizado com sucesso'
        },
        '500': {
            'description': 'Erro ao atualizar pedido'
        }
    }
})
def atualizar_pedido_rota(id_pedido: int):
    """Rota para atualizar um pedido por ID."""
    try:
        logger.info(f'Atualizando pedido com ID: {id_pedido}')
        body = request.get_json()
        pedido = Pedidos(**body)
        PedidoService.atualizar_pedido(id_pedido, pedido)
        return jsonify({'message': 'Pedido atualizado com sucesso'}), 200
    except Exception as e:
        logger.error(f'Erro ao atualizar pedido com ID {id_pedido}: {e}')
        return jsonify({'error': str(e)}), 500


@app.route('/pedidos/<int:id_pedido>', methods=['DELETE'])
@swag_from({
    'summary': 'Exclui um pedido por ID',
    'parameters': [
        {
            'name': 'id_pedido',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do pedido'
        }
    ],
    'responses': {
        '204': {
            'description': 'Pedido excluído com sucesso'
        },
        '500': {
            'description': 'Erro ao excluir pedido'
        }
    }
})
def excluir_pedido_rota(id_pedido: int):
    """Rota para excluir um pedido por ID."""
    try:
        logger.info(f'Excluindo pedido com ID: {id_pedido}')
        PedidoService.excluir_pedido(id_pedido)
        return '', 204
    except Exception as e:
        logger.error(f'Erro ao excluir pedido com ID {id_pedido}: {e}')
        return jsonify({'error': str(e)}), 500


@app.route('/')
def redirect_to_swagger():
    """Redireciona para a página do Swagger UI."""
    return redirect('/apidocs/')


if __name__ == '__main__':
    init_database()
    app.run(host='0.0.0.0', port=5003)
