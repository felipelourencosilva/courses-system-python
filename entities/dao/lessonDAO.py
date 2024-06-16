from entities.dao.abstractDAO import AbstractDAO


class LessonDAO(AbstractDAO):
    def __init__(self):
        super().__init__("pkl/lessons.pkl")