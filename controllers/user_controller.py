from views.user_view import *
from controllers.system_controller import *
from entities.user import *


class UserController:
    def __init__(self, system_controller: SystemController):
        self.__users = []
        self.__user_view = UserView()
        self.__system_controller = system_controller

    def get_user_by_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for user in self.__users:
                if (user.cpf == cpf):
                    return user
        return None

    def add_user(self):
        user_data = self.__user_view.get_add_user_data()
        user = User(user_data["name"], user_data["surname"],
                    user_data["email"], user_data["password"], user_data["cpf"])
        self.__users.append(user)

    def edit_user(self):
        self.list_users()
        user_cpf = self.__user_view.read_cpf()
        user = self.get_user_by_cpf(user_cpf)

        if (user is not None):
            user_data = self.__user_view.get_edit_user_data()
            user.nome = user_data["name"]
            user.surname = user_data["surname"]
            user.email = user_data["email"]
            user.password = user_data["password"]
        else:
            self.__user_view.show_message("Usuário não encontrado")

    def list_users(self):
        for user in self.__users:
            self.__user_view.show_user({"nome": user.name + " " + user.surname, "email": user.email, "senha": user.password, "cpf": user.cpf})

    def remove_user(self):
        self.list_users()
        user_cpf = self.__user_view.read_cpf()
        user = self.get_user_by_cpf(user_cpf)

        if (user is not None):
            self.__users.remove(user)
        else:
            self.__user_view.show_message("Usuário não encontrado")

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        lista_opcoes = {1: self.incluir_amigo, 2: self.alterar_amigo, 3: self.lista_amigos, 4: self.excluir_amigo,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_amigo.tela_opcoes()]()

    def show_view(self):
        options = {
            1: self.add_user(),
            2: self.remove_user(),
            3: self.edit_user(),
            4: self.list_users(),
            0: self.exit
        }

        while True:
            chosen_option = self.__user_view.view_options()
            options[chosen_option]()
