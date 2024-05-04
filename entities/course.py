from producer import *


class Course:
    def __init__(self, name: str, producer: Producer, description: str, price: float, comission_percentage: int):
        if isinstance(name, str):
            self.__name = name
        if isinstance(producer, Producer):
            self.__producer = producer
        if isinstance(description, str):
            self.__description = description
        if isinstance(price, float):
            self.__price = price
        if isinstance(comission_percentage, int):
            self.__comission_percentage = comission_percentage

        self.__comission_price = (self.__comission_percentage/100) * self.__price

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
    def comission_percentage(self) -> int:
        return self.__comission_percentage

    @comission_percentage.setter
    def comission_percentage(self, comission_percentage: int):
        if isinstance(comission_percentage, int):
            self.__comission_percentage = comission_percentage
            self.__comission_price = (self.__comission_percentage / 100) * self.__price

    @property
    def comission_price(self) -> float:
        return self.__comission_price

    def add_module(self):
        pass

    def remove_module(self):
        pass
