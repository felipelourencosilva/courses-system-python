from views.user_view import *
from entities.user import *
from entities.course import *

class UserController:
    __instance = None
    def __init__(self, system_controller):
        self.__users = []
        self.__user_view = UserView()
        self.__system_controller = system_controller

    '''
    def __new__(cls):
        if UserController.__instance is None:
            UserController.__instance = object.__new__(cls)
        return UserController.__instance
    '''

    def get_user_by_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for user in self.__users:
                if user.cpf == cpf:
                    return user

            producer = self.__system_controller.producer_controller.get_producer_by_cpf(cpf)
            if producer is not None:
                return producer

            affiliate = self.__system_controller.affiliate_controller.get_affiliate_by_cpf(cpf)
            if affiliate is not None:
                return affiliate

        return None

    def get_users(self):
        return (self.__users
                + self.__system_controller.producer_controller.get_producers()
                + self.__system_controller.affiliate_controller.get_affiliates()
        )

    def get_proper_users(self):
        return self.__users

    def add_user(self):
        user_data = self.__user_view.get_edit_user_data()
        '''while True:
            cpf = self.__user_view.read_cpf()
            if self.get_user_by_cpf(cpf) is not None:
                self.__user_view.show_message("Este CPF já foi utilizado.")
            else:
                user_data["cpf"] = cpf
                break'''
        user = User(user_data["name"], user_data["surname"],
                    user_data["email"], user_data["password"], user_data["cpf"])
        self.__users.append(user)
        self.__user_view.show_success_message("Usuário cadastrado com sucesso")

    def edit_user(self):
        self.list_users()
        if len(self.__users) == 0:
            return
        user_cpf = self.__user_view.read_cpf("Digite o CPF do usuário que deseja atualizar")
        user = self.get_user_by_cpf(user_cpf)

        if user is not None:
            user_data = self.__user_view.get_edit_user_data()
            user.name = user_data["name"]
            user.surname = user_data["surname"]
            user.email = user_data["email"]
            user.password = user_data["password"]
            self.__user_view.show_success_message("Usuário editado com sucesso")
        else:
            self.__user_view.show_message("Usuário não encontrado")

    def list_users(self):
        if len(self.__users) == 0:
            self.__user_view.show_message("Não há usuários cadastrados")
        else:
            for user in self.__users:
                course_names = [c.name for c in user.courses]
                self.__user_view.show_user({"name": user.name + " " + user.surname, "email": user.email,
                                            "password": user.password, "cpf": user.cpf, "balance": user.balance,
                                            "courses": course_names})

    def remove_user(self):
        self.list_users()
        if len(self.__users) == 0:
            return

        user_cpf = self.__user_view.read_cpf("Digite o CPF do usuário que deseja remover")
        user = self.get_user_by_cpf(user_cpf)

        if user is not None:
            self.__users.remove(user)
            self.__user_view.show_success_message("Usuário removido com sucesso")
        else:
            self.__user_view.show_message("Usuário não encontrado")

    def user_has_course(self, cpf: int, course: Course):
        if isinstance(cpf, int) and isinstance(course, Course):
            user = self.get_user_by_cpf(cpf)
            return user.has_course(course)
        return False

    def user_has_enough_balance(self, cpf: int, course: Course):
        if isinstance(cpf, int) and isinstance(course, Course):
            user = self.get_user_by_cpf(cpf)
            return user.balance >= course.price
        return False

    def user_add_course(self, cpf: int, course: Course):
        if isinstance(cpf, int) and isinstance(course, Course):
            user = self.get_user_by_cpf(cpf)
            user.add_course(course)

    def add_balance(self):
        if (
            len(self.__users) == 0
            and len(self.__system_controller.producer_controller.get_producers()) == 0
            and len(self.__system_controller.affiliate_controller.get_affiliates()) == 0
        ):
            self.__user_view.show_message("Não é possível adicionar saldo sem usuários no sistema")
            return

        if len(self.__users):
            self.list_users()
        if len(self.__system_controller.producer_controller.get_producers()):
            self.__system_controller.producer_controller.list_producer()
        if len(self.__system_controller.affiliate_controller.get_affiliates()):
            self.__system_controller.affiliate_controller.list_affiliates()

        user_cpf = self.__user_view.read_cpf()
        user = self.get_user_by_cpf(user_cpf)
        if user is None:
            self.__user_view.show_message("Usuário não encontrado")
            return
        value = self.__user_view.read_value("Digite o valor que deseja adicionar: ", "O valor precisa ser um número decimal maior que 0 (separado por '.')")
        user.add_balance(value)
        self.__user_view.show_success_message("Saldo adicionado com sucesso")

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_user,
            2: self.remove_user,
            3: self.edit_user,
            4: self.list_users,
            5: self.add_balance,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__user_view.view_options()
            options[chosen_option]()
