from views.abstract_view import AbstractView
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()


class SaleView(AbstractView):

    def __init__(self):
        pass

    def show_single_report(self, msg: str):
        table = Table(box=box.ROUNDED, border_style="#6D7280")
        table.add_column("Relatório", justify="center", style="#54cdc1")
        table.add_row(msg)

        print()
        console.print(table)
        print()

    def show_complete_report(self, messages: list):
        table = Table(box=box.ROUNDED, border_style="#6D7280")
        table.add_column("Relatório", justify="center", style="#54cdc1")
        for msg in messages:
            table.add_row(msg)

        print()
        console.print(table)
        print()

    def view_options(self) -> int:
        options = {
            1: "Gerar relatório completo",
            2: "Mostrar Curso mais vendido",
            3: "Mostrar Curso com maior lucro",
            4: "Mostrar Usuário com mais cursos",
            5: "Mostrar Produtor com mais vendas",
            6: "Mostrar Produtor com maior lucro",
            7: "Mostrar Afiliado com mais vendas",
            8: "Mostrar Afiliado com maior lucro",
            0: "Voltar"
        }
        return super().view_options("RELATÓRIOS", options)
