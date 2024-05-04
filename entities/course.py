from producer import *


class Course:
    def __init__(self, name: str, producer: Producer, description: str, price: float, commission_percentage: int):
        if isinstance(name, str):
            self.__name = name
        if isinstance(producer, Producer):
            self.__producer = producer
        if isinstance(description, str):
            self.__description = description
        if isinstance(price, float):
            self.__price = price
        if isinstance(commission_percentage, int):
            self.__commission_percentage = commission_percentage

        self.__commission_price = (self.__commission_percentage/100) * self.__price

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

    def add_module(self):
        pass

    def remove_module(self):
        pass
