import sqlite3
import json

from src.model.Pedidos import Pedidos


class PedidoDBService:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pedidos (
                id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                produtos TEXT
            )
        ''')
        self.conn.commit()

    def salvar_pedido(self, pedido: Pedidos):
        cursor = self.conn.cursor()
        produtos_json = json.dumps([produto.dict() for produto in pedido.produtos])
        cursor.execute('''
            INSERT INTO Pedidos (produtos) VALUES (?)
        ''', (produtos_json,))
        pedido.id_pedido = cursor.lastrowid
        self.conn.commit()

    def obter_pedido(self, id_pedido: int):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM Pedidos WHERE id_pedido = ?
        ''', (id_pedido,))
        pedido_row = cursor.fetchone()
        if not pedido_row:
            return None
        produtos = [Pedidos.Produtos(**produto) for produto in json.loads(pedido_row['produtos'])]
        return Pedidos(id_pedido=pedido_row['id_pedido'], produtos=produtos)

    def atualizar_pedido(self, id_pedido: int, pedido: Pedidos):
        cursor = self.conn.cursor()
        produtos_json = json.dumps([produto.dict() for produto in pedido.produtos])
        cursor.execute('''
            UPDATE Pedidos SET produtos = ? WHERE id_pedido = ?
        ''', (produtos_json, id_pedido))
        self.conn.commit()

    def excluir_pedido(self, id_pedido: int):
        cursor = self.conn.cursor()
        cursor.execute('''
            DELETE FROM Pedidos WHERE id_pedido = ?
        ''', (id_pedido,))
        self.conn.commit()


def init_database():
    with PedidoDBService(db_path='Pedidos.db') as db:
        db.create_tables()
