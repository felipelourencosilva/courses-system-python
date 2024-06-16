from entities.dao.abstractDAO import AbstractDAO


class ModuleDAO(AbstractDAO):
    def __init__(self):
        super().__init__("pkl/modules.pkl")