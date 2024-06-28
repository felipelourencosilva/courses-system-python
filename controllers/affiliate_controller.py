from exceptions.empty_input_exception import EmptyInputException
from exceptions.wrong_input_exception import WrongInputException
from views.affiliate_view import *
from entities.affiliate import *
from exceptions.user_not_found_exception import UserNotFoundException


class AffiliateController:
    __instance = None

    def __init__(self, system_controller):
        self.__affiliates = []
        self.__affiliate_view = AffiliateView()
        self.__system_controller = system_controller

    '''
    def __new__(cls):
        if AffiliateController.__instance is None:
            AffiliateController.__instance = object.__new__(cls)
        return AffiliateController.__instance
    '''

    def get_affiliates(self):
        return self.__affiliates

    def get_affiliate_by_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for affiliate in self.__affiliates:
                if affiliate.cpf == cpf:
                    return affiliate
        raise UserNotFoundException("Afiliado não encontrado.")

    def add_affiliate(self):
        affiliate_data = self.__affiliate_view.get_add_affiliate_data()

        if affiliate_data is None:
            return

        if (affiliate_data["name"] == "" or affiliate_data["surname"] == "" or affiliate_data["email"] == "" or
                affiliate_data["cpf"] == "" or affiliate_data["password"] == ""):
            raise EmptyInputException()

        if "@" not in affiliate_data["email"] or ".com" not in affiliate_data["email"]:
            raise WrongInputException('Email inválido. Deve conter "@" e ".com".')

        if len(affiliate_data["password"]) < 4:
            raise WrongInputException('A senha deve ter 4 ou mais caracteres')

        if not affiliate_data["cpf"].isdigit():
            raise WrongInputException('CPF precisa ser um número.')

        affiliate = Affiliate(
            affiliate_data["name"],
            affiliate_data["surname"],
            affiliate_data["email"],
            affiliate_data["password"],
            int(affiliate_data["cpf"])
        )
        self.__affiliates.append(affiliate)
        self.__affiliate_view.show_success_message("Afiliado cadastrado com sucesso")

    def edit_affiliate(self):
        affiliate_cpf = self.list_affiliates()

        if affiliate_cpf is None:
            return

        affiliate_cpf = int(affiliate_cpf)
        affiliate = self.get_affiliate_by_cpf(affiliate_cpf)
        affiliate_data = self.__affiliate_view.get_edit_affiliate_data()

        if affiliate_data is None:
            return

        if (affiliate_data["name"] == "" or affiliate_data["surname"] == "" or affiliate_data["email"] == "" or
                affiliate_data["password"] == ""):
            raise EmptyInputException()

        if "@" not in affiliate_data["email"] or ".com" not in affiliate_data["email"]:
            raise WrongInputException('Email inválido. Deve conter "@" e ".com".')

        if len(affiliate_data["password"]) < 4:
            raise WrongInputException('A senha deve ter 4 ou mais caracteres')

        if not affiliate_data["cpf"].isdigit():
            raise WrongInputException('CPF precisa ser um número.')

        affiliate.name = affiliate_data["name"]
        affiliate.surname = affiliate_data["surname"]
        affiliate.email = affiliate_data["email"]
        affiliate.password = affiliate_data["password"]
        self.__affiliate_view.show_success_message("Afiliado editado com sucesso")

    def list_affiliates(self):
        if len(self.__affiliates) == 0:
            self.__affiliate_view.show_message("Não há afiliados cadastrados")
        else:
            affiliates_data = []
            for affiliate in self.__affiliates:
                affiliates_data.append([
                    affiliate.name + " " + affiliate.surname,
                    affiliate.email,
                    affiliate.password,
                    affiliate.cpf,
                    affiliate.balance
                ])

            return self.__affiliate_view.show_affiliates(affiliates_data)

    def remove_affiliate(self):
        affiliate_cpf = self.list_affiliates()

        if affiliate_cpf is None:
            return

        affiliate = self.get_affiliate_by_cpf(affiliate_cpf)
        self.__affiliates.remove(affiliate)
        self.__affiliate_view.show_success_message("Afiliado removido com sucesso")

    def add_balance(self):
        affiliate_cpf = self.list_affiliates()
        if affiliate_cpf is None:
            return
        try:
            affiliate = self.get_affiliate_by_cpf(affiliate_cpf)
        except UserNotFoundException as e:
            self.__affiliate_view.show_message(e)
            return
        value = self.__affiliate_view.read_value("Digite o valor que deseja adicionar: ")
        affiliate.add_balance(value)
        self.__affiliate_view.show_success_message("Saldo adicionado com sucesso")

    def pay_affiliate(self, course, affiliate):
        if affiliate is not None:
            affiliate.add_balance(course.commission_price)

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_affiliate,
            2: self.remove_affiliate,
            3: self.edit_affiliate,
            4: self.list_affiliates,
            5: self.add_balance,
            0: self.previous_view
        }
        while True:
            chosen_option = self.__affiliate_view.view_options()
            options[chosen_option]()
