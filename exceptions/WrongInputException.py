class WrongInputException(Exception):

    def __init__(self):
        super().__init__("O Email deve conter '@' e '.com'.")