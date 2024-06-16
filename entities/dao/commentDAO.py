from entities.dao.abstractDAO import AbstractDAO


class CommentDAO(AbstractDAO):
    def __init__(self):
        super().__init__("comments.pkl")