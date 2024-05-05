from entities.user import *


class Producer(User):
    def __init__(self, name: str, surname: str, email: str, password: str, cpf: int):
        super().__init__(name, surname, email, password, cpf)

        self.__course = []
    def get_paid(self, amount: float):
        if isinstance(amount, float):
            self.__balance += amount

    def rescue(self, amount: float):
        if isinstance(amount, float):
            rescue_amount = min(amount, self.__balance)
            # just suppose the money is sent to a bank account
            self.__balance -= rescue_amount

    def add_course(self, course):
        self.__course.append(course)