from entities.dao.abstractDAO import AbstractDAO


class SaleDAO(AbstractDAO):
    def __init__(self):
        super().__init__("pkl/sales.pkl")