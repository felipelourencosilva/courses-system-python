from entities.user import *


class Comment:
    def __init__(self, author: User, comment: str, id: int):
        if isinstance(author, User):
            self.__author = author
        if isinstance(comment, str):
            self.__comment = comment
        if isinstance(id, int):
            self.__id = id

    @property
    def author(self) -> User:
        return self.__author

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        if isinstance(comment, str):
            self.__comment = comment

    @property
    def id(self) -> int:
        return self.__id

    def __str__(self):
        return str(self.__author.name) + " " + str(self.__author.surname) + ": " + str(self.__comment)