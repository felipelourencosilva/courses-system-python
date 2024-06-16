from views.abstract_view import AbstractView
import PySimpleGUI as sg
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()


class SaleView(AbstractView):

    def __init__(self):
        self.__windowSelf = None

    def show_single_report(self, msg: str):
        sg.ChangeLookAndFeel('LightGray1')
        layout = [
            [sg.Text(f"tmnc", font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='name')],
            [sg.Text('Sobrenome:', size=(15, 1)), sg.InputText('', key='surname')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', key='password')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__windowSelf = sg.Window('Dados usuário').Layout(layout)

        button, values = self.openSelf()

        self.closeSelf()

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

    def closeSelf(self):
        self.__windowSelf.Close()

    def openSelf(self):
        button, values = self.__windowSelf.Read()
        return button, values
