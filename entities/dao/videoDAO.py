from entities.dao.abstractDAO import AbstractDAO


class VideoDAO(AbstractDAO):
    def __init__(self):
        super().__init__("pkl/videos.pkl")
