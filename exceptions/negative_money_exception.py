class NegativeMoneyException(Exception):

    def __init__(self):
        super().__init__("A quantidade de dinheiro deve ser positiva.")
