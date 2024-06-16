from entities.dao.abstractDAO import AbstractDAO


class CourseDAO(AbstractDAO):
    def __init__(self):
        super().__init__("pkl/courses.pkl")