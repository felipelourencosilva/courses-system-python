from exceptions.empty_input_exception import EmptyInputException
from exceptions.missing_entity_exception import MissingEntityException
from exceptions.wrong_input_exception import WrongInputException
from views.user_view import *
from entities.course import *
from exceptions.user_not_found_exception import UserNotFoundException


class UserController:
    __instance = None

    def __init__(self, system_controller):
        self.__users = []
        self.__user_view = UserView()
        self.__system_controller = system_controller

    def __new__(cls, *args, **kwargs):
        if UserController.__instance is None:
            UserController.__instance = super(UserController, cls).__new__(cls)
        return UserController.__instance

    def get_user_by_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for user in self.__users:
                if user.cpf == cpf:
                    return user
            try:
                return self.__system_controller.producer_controller.get_producer_by_cpf(cpf)
            except UserNotFoundException:
                pass

            try:
                return self.__system_controller.affiliate_controller.get_affiliate_by_cpf(cpf)
            except UserNotFoundException:
                pass

        raise UserNotFoundException

    def get_users(self):
        return (self.__users
                + self.__system_controller.producer_controller.get_producers()
                + self.__system_controller.affiliate_controller.get_affiliates()
                )

    def get_proper_users(self):
        return self.__users

    def add_user(self):
        try:
            user_data = self.__user_view.get_add_user_data()

            if user_data is None:
                return

            if (user_data["name"] == "" or user_data["surname"] == "" or user_data["email"] == "" or
                    user_data["cpf"] == "" or user_data["password"] == ""):
                raise EmptyInputException()

            if "@" not in user_data["email"] or ".com" not in user_data["email"]:
                raise WrongInputException('Email inválido. Deve conter "@" e ".com".')

            if len(user_data["password"]) < 4:
                raise WrongInputException('A senha deve ter 4 ou mais caracteres')

            if not user_data["cpf"].isdigit():
                raise WrongInputException('CPF precisa ser um número.')

            cpf = int(user_data["cpf"])
            for user in self.get_users():
                if user.cpf == cpf:
                    raise WrongInputException('Este CPF já foi utilizado.')

            user = User(
                user_data["name"],
                user_data["surname"],
                user_data["email"],
                user_data["password"],
                cpf
            )

            self.__users.append(user)
            self.__user_view.show_success_message("Usuário cadastrado com sucesso")
        except (WrongInputException, EmptyInputException) as e:
            self.__user_view.show_message(e)

    def edit_user(self):
        try:
            user_cpf = self.list_users()

            if user_cpf is None:
                return

            user_cpf = int(user_cpf)
            user = self.get_user_by_cpf(user_cpf)
            user_info = {"name": user.name, "surname": user.surname, "email": user.email,
                         "password": user.password}
            user_data = self.__user_view.get_edit_user_data(user_info)

            if user_data is None:
                return

            if (user_data["name"] == "" or user_data["surname"] == "" or user_data["email"] == "" or
                    user_data["password"] == ""):
                raise EmptyInputException()

            if "@" not in user_data["email"] or ".com" not in user_data["email"]:
                raise WrongInputException('Email inválido. Deve conter "@" e ".com".')

            if len(user_data["password"]) < 4:
                raise WrongInputException('A senha deve ter 4 ou mais caracteres')

            user.name = user_data["name"]
            user.surname = user_data["surname"]
            user.email = user_data["email"]
            user.password = user_data["password"]
            self.__user_view.show_success_message("Usuário editado com sucesso")
        except (WrongInputException, EmptyInputException) as e:
            self.__user_view.show_message(e)

    def list_users(self):
        try:
            if len(self.get_users()) == 0:
                raise MissingEntityException("Não há usuários cadastrados")

            users_info = []
            for user in self.get_users():
                course_names = [c.name for c in user.courses]
                users_info.append([
                    user.name + " " + user.surname,
                    user.email,
                    user.password,
                    user.cpf,
                    user.balance,
                    ", ".join(course_names)
                ])

            return self.__user_view.show_users(users_info)  # should return user cpf
        except MissingEntityException as e:
            self.__user_view.show_message(e)

    def remove_user(self):
        user_cpf = self.list_users()

        if user_cpf is None:
            return

        user = self.get_user_by_cpf(user_cpf)
        self.__users.remove(user)
        self.__user_view.show_success_message("Usuário removido com sucesso.")

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
        try:
            if len(self.get_users()) == 0:
                raise MissingEntityException("Não é possível adicionar saldo sem usuários no sistema")

            user_cpf = self.list_users()
            if user_cpf is None:
                return

            user = self.get_user_by_cpf(user_cpf)
            value = self.__user_view.read_value("Digite o valor que deseja adicionar: ")
            if value is None:
                return

            if not value.isdigit() or float(value) < 0:
                raise WrongInputException("Digite o valor corretamente")

            value = float(value)
            user.add_balance(value)
            self.__user_view.show_success_message("Saldo adicionado com sucesso")
        except (WrongInputException, MissingEntityException) as e:
            self.__user_view.show_message(e)

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
