from entities.dao.abstractDAO import AbstractDAO


class ProducerDAO(AbstractDAO):
    def __init__(self):
        super().__init__("producers.pkl")