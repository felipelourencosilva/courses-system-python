from views.producer_view import *
from entities.producer import *


class ProducerController:
    __instance = None
    def __init__(self, system_controller):
        self.__producers = []
        self.__producer_view = ProducerView()
        self.__system_controller = system_controller

    '''
    def __new__(cls):
        if ProducerController.__instance is None:
            ProducerController.__instance = object.__new__(cls)
        return ProducerController.__instance
    '''
    def get_producers(self):
        return self.__producers

    def get_producer_by_cpf(self, cpf: int):
        if isinstance(cpf, int):
            for producer in self.__producers:
                if producer.cpf == cpf:
                    return producer
        return None

    def add_producer(self):
        producer_data = self.__producer_view.get_edit_producer_data()

        while True:
            cpf = self.__producer_view.read_cpf()
            if self.__system_controller.user_controller.get_user_by_cpf(cpf) is not None:
                self.__producer_view.show_message("Este CPF já foi utilizado.")
            else:
                producer_data["cpf"] = cpf
                break

        producer = Producer(producer_data["name"], producer_data["surname"],
                            producer_data["email"], producer_data["password"], producer_data["cpf"])
        self.__producers.append(producer)
        self.__producer_view.show_success_message("Produtor cadastrado com sucesso")

    def edit_producer(self):
        self.list_producer()
        if len(self.__producers) == 0:
            return
        producer_cpf = self.__producer_view.read_cpf()
        producer = self.get_producer_by_cpf(producer_cpf)

        if producer is not None:
            producer_data = self.__producer_view.get_edit_producer_data()
            producer.name = producer_data["name"]
            producer.surname = producer_data["surname"]
            producer.email = producer_data["email"]
            producer.password = producer_data["password"]
            self.__producer_view.show_success_message("Produtor editado com sucesso")
        else:
            self.__producer_view.show_message("Produtor não encontrado")

    def list_producer(self):
        if len(self.__producers) == 0:
            self.__producer_view.show_message("Não há produtores cadastrados")
        else:
            for producer in self.__producers:
                self.__producer_view.show_producer({"name": producer.name + " " + producer.surname,
                                                    "email": producer.email, "password": producer.password,
                                                    "cpf": producer.cpf, "balance": producer.balance})

    def remove_producer(self):
        self.list_producer()
        if len(self.__producers) == 0:
            return
        producer_cpf = self.__producer_view.read_cpf()
        producer = self.get_producer_by_cpf(producer_cpf)

        if producer is not None:
            self.__producers.remove(producer)
            self.__producer_view.show_success_message("Produtor removido com sucesso")
        else:
            self.__producer_view.show_message("Produtor não encontrado")

    def add_balance(self):
        self.list_producer()
        if len(self.__producers) == 0:
            return
        producer_cpf = self.__producer_view.read_cpf()
        producer = self.get_producer_by_cpf(producer_cpf)
        value = self.__producer_view.read_value("Digite o valor que deseja adicionar: ",
                                            "O valor precisa ser um número decimal maior que 0 (separado por '.')")

        if producer is not None:
            producer.add_balance(value)
            self.__producer_view.show_success_message("Saldo adicionado com sucesso")
        else:
            self.__producer_view.show_message("Produtor não encontrado")

    def pay_producer(self, course, hasAffiliate):
        balance = course.price
        if hasAffiliate:
            balance -= course.commission_price
        course.producer.add_balance(balance)

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_producer,
            2: self.remove_producer,
            3: self.edit_producer,
            4: self.list_producer,
            5: self.add_balance,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__producer_view.view_options()
            options[chosen_option]()
