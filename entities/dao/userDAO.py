from entities.dao.abstractDAO import AbstractDAO


class UserDAO(AbstractDAO):
    def __init__(self):
        super().__init__("pkl/users.pkl")