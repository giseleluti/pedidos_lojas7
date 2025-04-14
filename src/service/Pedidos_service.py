import json


from src.repository.Database import PedidoDBService
from src.model import Pedidos
from flask import jsonify


class PedidoService:
    @staticmethod
    def criar_pedido(pedido: Pedidos):
        try:
            with PedidoDBService(db_path='Pedidos.db') as db:
                db.salvar_pedido(pedido)
            return jsonify(pedido.dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def obter_pedido(id_pedido: int):
        try:
            with PedidoDBService(db_path='Pedidos.db') as db:
                pedido = db.obter_pedido(id_pedido)
            if pedido:
                pedido_dict = {
                    "id_pedido": pedido.id_pedido,
                    "produtos": [
                        {
                            "id_produto": produto.id_produto,
                            "title": produto.title,
                            "price": produto.price
                        }
                        for produto in pedido.produtos
                    ]
                }
                pedido_json = json.dumps(pedido_dict)
                return pedido_json, 200
            else:
                return jsonify({'message': 'Pedido não encontrado'}), 404

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def atualizar_pedido(id_pedido: int, pedido: Pedidos):
        try:
            with PedidoDBService(db_path='Pedidos.db') as db:
                db.atualizar_pedido(id_pedido, pedido)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def excluir_pedido(id_pedido: int):
        try:
            with PedidoDBService(db_path='Pedidos.db') as db:
                db.excluir_pedido(id_pedido)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
