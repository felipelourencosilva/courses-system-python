class Comment:
    def __init__(author: User, comment: str):
        if isinstance(author, User):
            self.__author = author
        if isinstance(comment, str):
            self.__comment = comment

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
