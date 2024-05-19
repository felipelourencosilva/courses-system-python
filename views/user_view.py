from views.abstract_view import AbstractView
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()

class UserView(AbstractView):

    def __init__(self):
        pass

    def view_options(self):
        options = {
            1: "Adicionar Usuário",
            2: "Excluir Usuário",
            3: "Editar Usuário",
            4: "Listar Usuários",
            5: "Adicionar saldo ao Usuário",
            0: "Voltar"
        }
        return super().view_options("USUÁRIO", options)

    def get_edit_user_data(self):
        return super().read_basic_edit_user_data("USUÁRIO")

    def show_user(self, user_data):
        showUserTable = Table(box=box.ROUNDED, border_style="#6D7280")
        showUserTable.add_column("Usuário", justify="left", style="#54cdc1")
        showUserTable.add_column("Informações", justify="left", style="bold italic")
        showUserTable.add_row("Nome do usuário", str(user_data["name"]))
        showUserTable.add_row("Email do usuário", str(user_data["email"]))
        showUserTable.add_row("Senha do usuário", str(user_data["password"]))
        showUserTable.add_row("CPF do usuário", str(user_data["cpf"]))
        showUserTable.add_row("Saldo do usuário", str(user_data["balance"]))
        if len(user_data["courses"]) == 0:
            showUserTable.add_row("Cursos do usuário", "Nenhum")
        else:
            showUserTable.add_row("Cursos do usuário", ", ".join(user_data["courses"]))

        console.print(showUserTable)
        print()
