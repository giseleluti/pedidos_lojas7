from typing import List

from pydantic import BaseModel


class Pedidos(BaseModel):
    class Produtos(BaseModel):
        id_produto: int
        title: str
        price: float

    id_pedido: int = None
    produtos: List[Produtos]
