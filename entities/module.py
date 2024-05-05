class Module:
    def __init__(self, title: str, description: str, id: int):
        if isinstance(title, str):
            self.__title = title
        if isinstance(description, str):
            self.__description = description
        if isinstance(id, int):
            self.__id = id

        self.__lessons = []

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
    def lessons(self) -> list:
        return self.__lessons

    def add_lesson(self, lesson):
        self.__lessons.append(lesson)

    def remove_lesson(self, lesson):
        if lesson in self.__lessons:
            self.__lessons.remove(lesson)
