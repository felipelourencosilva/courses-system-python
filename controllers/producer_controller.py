from views.producer_view import *
from entities.producer import *
from exceptions.user_not_found_exception import UserNotFoundException


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
        raise UserNotFoundException("Produtor não encontrado.")

    def add_producer(self):
        producer_data = self.__producer_view.get_add_producer_data()
        if producer_data is None:
            return

        producer = Producer(producer_data["name"], producer_data["surname"],
                            producer_data["email"], producer_data["password"], int(producer_data["cpf"]))
        self.__producers.append(producer)
        self.__producer_view.show_success_message("Produtor cadastrado com sucesso")

    def edit_producer(self):
        producer_cpf = self.list_producer()
        if producer_cpf is None:
            return
        producer_cpf = int(producer_cpf)

        try:
            producer = self.get_producer_by_cpf(producer_cpf)
        except UserNotFoundException as e:
            self.__producer_view.show_message(e)
            return

        producer_data = self.__producer_view.get_edit_producer_data()
        if producer_data is None:
            return
        producer.name = producer_data["name"]
        producer.surname = producer_data["surname"]
        producer.email = producer_data["email"]
        producer.password = producer_data["password"]
        self.__producer_view.show_success_message("Produtor editado com sucesso")

    def list_producer(self):
        if len(self.__producers) == 0:
            self.__producer_view.show_message("Não há produtores cadastrados")
        else:
            producers_data = []
            for producer in self.__producers:
                producers_data.append([
                    producer.name + " " + producer.surname,
                    producer.email,
                    producer.password,
                    producer.cpf,
                    producer.balance
                ])

            return self.__producer_view.show_producers(producers_data)

    def remove_producer(self):
        producer_cpf = self.list_producer()
        if producer_cpf is None:
            return

        try:
            producer = self.get_producer_by_cpf(producer_cpf)
        except UserNotFoundException as e:
            self.__producer_view.show_message(e)
            return
        self.__producers.remove(producer)
        self.__producer_view.show_success_message("Produtor removido com sucesso")

    def add_balance(self):
        producer_cpf = self.list_producer()
        if producer_cpf is None:
            return
        try:
            producer = self.get_producer_by_cpf(producer_cpf)
        except UserNotFoundException as e:
            self.__producer_view.show_message(e)
            return
        value = self.__producer_view.read_value("Digite o valor que deseja adicionar: ")
        producer.add_balance(value)
        self.__producer_view.show_success_message("Saldo adicionado com sucesso")

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
