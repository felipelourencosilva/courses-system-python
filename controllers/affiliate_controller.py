from views.affiliate_view import *
from entities.affiliate import *


class AffiliateController:
    def __init__(self, system_controller):
        self.__affiliates = []
        self.__affiliate_view = AffiliateView()
        self.__system_controller = system_controller

    def get_affiliates(self):
        return self.__affiliates

    def get_affiliate_by_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for affiliate in self.__affiliates:
                if affiliate.cpf == cpf:
                    return affiliate
        return None

    def add_affiliate(self):
        affiliate_data = self.__affiliate_view.get_edit_affiliate_data()
        while True:
            cpf = self.__affiliate_view.read_cpf()
            for affiliate in self.__affiliates:
                if affiliate.cpf == cpf:
                    self.__affiliate_view.show_message("Este CPF já foi utilizado.")
                    break
            else: #nobreak
                affiliate_data["cpf"] = cpf
                break
        affiliate = Affiliate(affiliate_data["name"], affiliate_data["surname"],
                              affiliate_data["email"], affiliate_data["password"], affiliate_data["cpf"])
        self.__affiliates.append(affiliate)

    def edit_affiliate(self):
        self.list_affiliates()
        if len(self.__affiliates) == 0:
            return
        affiliate_cpf = self.__affiliate_view.read_cpf()
        affiliate = self.get_affiliate_by_cpf(affiliate_cpf)

        if affiliate is not None:
            affiliate_data = self.__affiliate_view.get_edit_affiliate_data()
            affiliate.name = affiliate_data["name"]
            affiliate.surname = affiliate_data["surname"]
            affiliate.email = affiliate_data["email"]
            affiliate.password = affiliate_data["password"]
        else:
            self.__affiliate_view.show_message("Afiliado não encontrado")

    def list_affiliates(self):
        if len(self.__affiliates) == 0:
            self.__affiliate_view.show_message("Não há afiliados cadastrados")
        else:
            for affiliate in self.__affiliates:
                self.__affiliate_view.show_affiliate({
                    "name": affiliate.name + " " + affiliate.surname,
                    "email": affiliate.email,
                    "password": affiliate.password,
                    "cpf": affiliate.cpf,
                    "balance": affiliate.balance
                    }
                )

    def remove_affiliate(self):
        self.list_affiliates()
        if len(self.__affiliates) == 0:
            return
        affiliate_cpf = self.__affiliate_view.read_cpf()
        affiliate = self.get_affiliate_by_cpf(affiliate_cpf)

        if affiliate is not None:
            self.__affiliates.remove(affiliate)
        else:
            self.__affiliate_view.show_message("Afiliado não encontrado")

    def add_balance(self):
        self.list_affiliates()
        if len(self.__affiliates) == 0:
            return
        producer_cpf = self.__affiliate_view.read_cpf()
        affiliate = self.get_affiliate_by_cpf(producer_cpf)
        value = self.__affiliate_view.read_value("Digite o valor que deseja adicionar: ", "O valor precisa ser um número decimal maior que 0 (separado por '.')")

        if affiliate is not None:
            affiliate.add_balance(value)
        else:
            self.__affiliate_view.show_message("Afiliado não encontrado")

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

