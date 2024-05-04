from views.affiliate_view import *
from entities.affiliate import *


class AffiliateController:
    def __init__(self, system_controller):
        self.__affiliates = []
        self.__affiliate_view = AffiliateView()
        self.__system_controller = system_controller

    def get_affiliate_by_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for affiliate in self.__affiliates:
                if affiliate.cpf == cpf:
                    return affiliate
        return None

    def add_affiliate(self):
        affiliate_data = self.__affiliate_view.get_add_affiliate_data()
        affiliate = Affiliate(affiliate_data["name"], affiliate_data["surname"],
                              affiliate_data["email"], affiliate_data["password"], affiliate_data["cpf"])
        self.__affiliates.append(affiliate)

    def edit_affiliate(self):
        self.list_affiliates()
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
                    "cpf": affiliate.cpf
                    }
                )

    def remove_affiliate(self):
        self.list_affiliates()
        affiliate_cpf = self.__affiliate_view.read_cpf()
        affiliate = self.get_affiliate_by_cpf(affiliate_cpf)

        if affiliate is not None:
            self.__affiliates.remove(affiliate)
        else:
            self.__affiliate_view.show_message("Afiliado não encontrado")

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_affiliate,
            2: self.remove_affiliate,
            3: self.edit_affiliate,
            4: self.list_affiliates,
            0: self.previous_view
        }
        while True:
            chosen_option = self.__affiliate_view.view_options()
            options[chosen_option]()

