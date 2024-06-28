class User:
    def __init__(self, name: str, surname: str, email: str, password: str, cpf: int):
        if isinstance(name, str):
            self.__name = name
        if isinstance(surname, str):
            self.__surname = surname
        if isinstance(email, str):
            self.__email = email
        if isinstance(password, str):
            self.__password = password
        if isinstance(cpf, int):
            self.__cpf = cpf
        self.__description = ""
        self.__courses = []
        self.__balance = 0.0

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
    def email(self, email):
        if isinstance(email, str):
            self.__email = email

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password):
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
    def cpf(self) -> int:
        return self.__cpf

    @property
    def courses(self) -> list:
        return self.__courses

    @property
    def balance(self) -> float:
        return self.__balance

    def add_course(self, course):
        self.__courses.append(course)
        self.__balance -= course.price

    def has_course(self, course):
        return course in self.__courses

    def add_balance(self, value):
        self.__balance += value
