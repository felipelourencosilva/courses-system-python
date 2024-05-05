from views.user_view import *
from entities.user import *
from entities.course import *

class UserController:
    def __init__(self, system_controller):
        self.__users = []
        self.__user_view = UserView()
        self.__system_controller = system_controller

    def get_user_by_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for user in self.__users:
                if user.cpf == cpf:
                    return user
        return None

    def add_user(self):
        user_data = self.__user_view.get_add_user_data()
        user = User(user_data["name"], user_data["surname"],
                    user_data["email"], user_data["password"], user_data["cpf"])
        self.__users.append(user)

    def edit_user(self):
        self.list_users()
        if len(self.__users) == 0:
            return
        user_cpf = self.__user_view.read_cpf()
        user = self.get_user_by_cpf(user_cpf)

        if user is not None:
            user_data = self.__user_view.get_edit_user_data()
            user.name = user_data["name"]
            user.surname = user_data["surname"]
            user.email = user_data["email"]
            user.password = user_data["password"]
        else:
            self.__user_view.show_message("Usuário não encontrado")

    def list_users(self):
        if len(self.__users) == 0:
            self.__user_view.show_message("Não há usuários cadastrados")
        else:
            for user in self.__users:
                self.__user_view.show_user({"name": user.name + " " + user.surname, "email": user.email,
                                            "password": user.password, "cpf": user.cpf, "balance": user.balance})

    def remove_user(self):
        self.list_users()
        if len(self.__users) == 0:
            return
        user_cpf = self.__user_view.read_cpf()
        user = self.get_user_by_cpf(user_cpf)

        if user is not None:
            self.__users.remove(user)
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
        self.list_users()
        if len(self.__users) == 0:
            return
        user_cpf = self.__user_view.read_cpf()
        user = self.get_user_by_cpf(user_cpf)
        value = self.__user_view.read_value()

        if user is not None:
            user.add_balance(value)
        else:
            self.__user_view.show_message("Usuário não encontrado")

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
