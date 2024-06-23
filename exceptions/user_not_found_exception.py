class UserNotFoundException(Exception):

    def __init__(self, msg = "Usuário não encontrado."):
        super().__init__(msg)
