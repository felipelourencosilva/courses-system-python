from video import *


class Lesson:
    def __init__(self, titulo: str, description: str, video: Video):
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(description, str):
            self.__description = description
        if isinstance(video, Video):
            self.__video = video

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if isinstance(description, str):
            self.__description = description

    @property
    def video(self) -> Video:
        return self.__video

    @video.setter
    def video(self, video: Video):
        if isinstance(video, Video):
            self.__video = video

    def add_comment(self):
        pass

    def remove_comment(self):
        pass
