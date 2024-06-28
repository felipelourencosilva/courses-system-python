class EmptyInputException(Exception):

    def __init__(self):
        super().__init__("É necessário preencher todos os campos.")
