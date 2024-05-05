from views.abstract_view import AbstractView


class ProducerView(AbstractView):

    def __init__(self):
        pass

    def view_options(self):
        options = {
            1: "Adicionar Produtor",
            2: "Excluir Produtor",
            3: "Editar Produtor",
            4: "Listar Produtores",
            0: "Voltar"
        }
        return super().view_options("PRODUTOR", options)

    def get_add_producer_data(self):
        return super().read_basic_add_user_data("PRODUTOR")

    def get_edit_producer_data(self):
        return super().read_basic_edit_user_data("PRODUTOR")

    def show_producer(self, producer_data):
        print("Nome do Produtor: ", producer_data["name"])
        print("Email do Produtor: ", producer_data["email"])
        print("Senha do Produtor: ", producer_data["password"])
        print("CPF do Produtor: ", producer_data["cpf"])
        print("Saldo do Produtor: ", producer_data["balance"])
        print()
