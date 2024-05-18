from views.abstract_view import AbstractView
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()


class AffiliateView(AbstractView):

    def __init__(self):
        pass
    def view_options(self) -> int:
        options = {
            1: "Adicionar Afiliado",
            2: "Excluir Afiliado",
            3: "Editar Afiliado",
            4: "Listar Afiliados",
            0: "Voltar"
        }
        return super().view_options("AFILIADO", options)

    def get_edit_affiliate_data(self):
        return super().read_basic_edit_user_data("AFILIADO")

    def show_affiliate(self, affiliate_data):
        showAffiliateTable = Table(box=box.ROUNDED, border_style="#6D7280")
        showAffiliateTable.add_column(justify="left", style="#54cdc1")
        showAffiliateTable.add_column("Informações", justify="left", style="bold italic")
        showAffiliateTable.add_row("Nome do afiliado: ", str(affiliate_data["name"]))
        showAffiliateTable.add_row("Email do afiliado: ", str(affiliate_data["email"]))
        showAffiliateTable.add_row("Senha do afiliado: ", str(affiliate_data["password"]))
        showAffiliateTable.add_row("CPF do afiliado: ", str(affiliate_data["cpf"]))
        showAffiliateTable.add_row("Saldo do afiliado: ", str(affiliate_data["balance"]))

        console.print(showAffiliateTable)
        print()
