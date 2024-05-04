class User:
    def __init__(self, name: str, surname: str, email: str, password: str, cpf: str):
        if isinstance(name, str):
            self.__name = name
        if isinstance(surname, str):
            self.__surname = surname
        if isinstance(email, str):
            self.__email = email
        if isinstance(password, str):
            self.__password = password
        if isinstance(cpf, str):
            self.__cpf = cpf
        self.__description = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str):
            self.__name = name

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        if isinstance(surname, str):
            self.__surname = surname

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email) -> str:
        if isinstance(email, str):
            self.__email = email

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password) -> str:
        if isinstance(password, str):
            self.__password = password

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if isinstance(description, str):
            self.__description = description

    @property
    def cpf(self) -> str:
        return self.__cpf

    def buy_course(self):
        pass
