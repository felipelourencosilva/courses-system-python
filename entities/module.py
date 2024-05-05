class Module:
    def __init__(self, title: str, description: str, id: int):
        if isinstance(title, str):
            self.__title = title
        if isinstance(description, str):
            self.__description = description
        if isinstance(id, int):
            self.__id = id

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

    def add_lesson(self):
        pass

    def remove_lesson(self):
        pass
