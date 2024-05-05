from entities.user import *

class Affiliate(User):
    def __init__(self, name: str, surname: str, email: str, password: str, cpf: int):
        super().__init__(name, surname, email, password, cpf)

    def get_paid(self, amount: float):
        if isinstance(amount, float):
            self.__balance += amount

    def rescue(self, amount: float):
        if isinstance(amount, float):
            rescue_amount = min(amount, self.__balance)
            # just suppose the money is sent to a bank account
            self.__balance -= rescue_amount