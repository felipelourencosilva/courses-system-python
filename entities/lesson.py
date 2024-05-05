from video import *


class Lesson:
    def __init__(self, title: str, description: str, video: Video):
        if isinstance(title, str):
            self.__title = title
        if isinstance(description, str):
            self.__description = description
        if isinstance(video, Video):
            self.__video = video

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

    def add_comment(self):
        pass

    def remove_comment(self):
        pass
