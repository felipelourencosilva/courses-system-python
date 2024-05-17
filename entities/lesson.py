from entities.video import *
from entities.comment import *


class Lesson:
    def __init__(self, title: str, description: str, video: Video, id: int):
        if isinstance(title, str):
            self.__title = title
        if isinstance(description, str):
            self.__description = description
        if isinstance(video, Video):
            self.__video = video
        if isinstance(id, int):
            self.__id = id

        self.__comments = []

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        if isinstance(title, str):
            self.__title = title

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

    @property
    def comments(self) -> list:
        return self.__comments

    def add_comment(self, comment: Comment):
        if isinstance(comment, Comment):
            self.__comments.append(comment)

    def remove_comment(self, comment: Comment):
        if comment in self.__comments:
            self.__comments.remove(comment)
