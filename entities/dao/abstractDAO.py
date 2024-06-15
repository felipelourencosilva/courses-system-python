from abc import ABC, abstractmethod


class AbstractDAO(ABC):
    @abstractmethod
    def __init__(self):
        pass