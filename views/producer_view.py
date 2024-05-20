from views.abstract_view import AbstractView
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()


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
        return super().view_options("PRODUTORES", options)

    def get_edit_producer_data(self):
        return super().read_basic_edit_user_data("PRODUTOR")

    def show_producer(self, producer_data):
        showProducerTable = Table(box=box.ROUNDED, border_style="#6D7280")
        showProducerTable.add_column("Produtor", justify="left", style="#54cdc1")
        showProducerTable.add_column("Informações", justify="left", style="bold italic")
        showProducerTable.add_row("Nome do Produtor", str(producer_data["name"]))
        showProducerTable.add_row("Email do Produtor", str(producer_data["email"]))
        showProducerTable.add_row("Senha do Produtor", str(producer_data["password"]))
        showProducerTable.add_row("CPF do Produtor", str(producer_data["cpf"]))
        showProducerTable.add_row("Saldo do Produtor", str(producer_data["balance"]))
        console.print(showProducerTable)

        print()
