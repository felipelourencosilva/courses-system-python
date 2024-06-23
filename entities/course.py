from entities.producer import *


class Course:
    def __init__(self, name: str, producer: Producer, description: str, price: float, commission_percentage: int, id: int):
        self.__name = name
        self.__producer = producer
        self.__description = description
        self.__price = price
        self.__commission_percentage = commission_percentage
        self.__id = id
        self.__commission_price = (commission_percentage/100) * price
        self.__modules = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str):
            self.__name = name

    @property
    def producer(self) -> Producer:
        return self.__producer

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if isinstance(description, str):
            self.__description = description

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        if isinstance(price, float):
            self.__price = price

    @property
    def commission_percentage(self) -> int:
        return self.__commission_percentage

    @commission_percentage.setter
    def commission_percentage(self, commission_percentage: int):
        if isinstance(commission_percentage, int):
            self.__commission_percentage = commission_percentage
            self.__commission_price = (self.__commission_percentage / 100) * self.__price

    @property
    def commission_price(self) -> float:
        return self.__commission_price

    @property
    def modules(self) -> list:
        return self.__modules

    def add_module(self, module):
        self.__modules.append(module)

    def remove_module(self, module):
        if module in self.__modules:
            self.__modules.remove(module)

    def __eq__(self, other):
        return self.__id == other.__id

    def __hash__(self):
        return hash(self.__id)
