from entities.dao.abstractDAO import AbstractDAO


class SystemDAO(AbstractDAO):

    def __init__(self):
        super().__init__("pkl/system_data.pkl")

