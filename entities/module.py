class Module:
    def __init__(self, titulo: str, description: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(description, str):
            self.__description = description

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

    def add_lesson(self):
        pass

    def remove_lesson(self):
        pass
