class NotEnoughBalanceException(Exception):

    def __init__(self):
        super().__init__("Saldo insuficiente.")
