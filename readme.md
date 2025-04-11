# API de Pedidos Baseada nos Produtos da Fakestore

## Descrição

Esta é uma API RESTful construída com Flask para gerenciar pedidos. Ela foi desenvolvida com base em um modelo de dados de produtos (presumivelmente da Fakestore API ou similar) e permite criar, buscar, atualizar e excluir pedidos. A API utiliza Flasgger para gerar a documentação Swagger UI, facilitando a exploração e o teste dos endpoints.

## Objetivo da API

Realizar o registro de todos os pedidos da API cacheada de produtos no banco de dados para processamento.

## Informações Gerais

* **Inicialização do Projeto:** O projeto foi configurado com Flask e Flasgger para criar a API e sua documentação interativa.
* **Modelo de Pedidos:** Foi definido um modelo de dados para pedidos (`src.model.Pedidos.Pedidos`), contendo informações como ID do pedido, itens do pedido (lista de produtos).
* **Persistência de Dados:** Utiliza SQLite para persistência de dados.
* **Endpoints da API:** Foram desenvolvidos os seguintes endpoints:
    * `POST /pedidos`: Cria um novo pedido.
    * `GET /pedidos/<id_pedido>`: Busca um pedido por seu ID.
    * `PUT /pedidos/<id_pedido>`: Atualiza um pedido existente por seu ID.
    * `DELETE /pedidos/<id_pedido>`: Exclui um pedido por seu ID.
    * `GET /`: Redireciona para a interface Swagger UI.
* **Documentação Swagger:** O Flasgger foi integrado para gerar automaticamente a documentação da API no formato Swagger UI, acessível em `/apidocs/`. A documentação inclui detalhes sobre os endpoints, parâmetros, corpos de requisição e respostas.
* **Logging:** A biblioteca `logging` do Python foi configurada para registrar informações, avisos e erros durante a execução da API, auxiliando na depuração e monitoramento.

## Requisitos

* Python 3.9 ou superior
* Pip (gerenciador de pacotes do Python)
* Docker (opcional, para execução em contêiner)

## Dependências

As seguintes bibliotecas Python são necessárias para executar a API:

pydantic~=2.10.6
flask~=3.0.3
flask_pydantic
flasgger

## Instalação

1. Clone o repositório e acesse a pasta:

   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd <nome_do_repositorio>
2. 
Crie um ambiente virtual (opcional, mas recomendado):
Bash
Copiar o código
python -m venv venv
3. 
Ative o ambiente virtual:
• 
No Windows:
Bash
Copiar o código
venv\Scripts\activate
• 
No macOS/Linux:
Bash
Copiar o código
source venv/bin/activate
4. 
Instale as dependências:
Bash
Copiar o código
pip install -r requirements.txt
Execução
1. 
Execute a aplicação:
Bash
Copiar o código
python app.py
A API estará disponível em http://0.0.0.0:5003.
2. 
Documentação Swagger UI:
Acesse a documentação interativa da API através do seu navegador em http://localhost:5003/apidocs/.
Execução com Docker (Opcional)
1. 
Construa a imagem Docker:
Bash
Copiar o código
docker build -t pedidos_lojas7 .
2. 
Execute o container:
Bash
Copiar o código
docker run -p 5003:5003 pedidos_lojas7
3. 
Acesse a aplicação em http://localhost:5003.