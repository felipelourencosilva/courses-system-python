from views.abstract_view import AbstractView
import PySimpleGUI as sg


class SaleView(AbstractView):

    def __init__(self):
        self.__windowSelf = None

    def show_single_report(self, msg: str):
        layout = [
            [sg.Text(f"{msg}", font=("Helvica", 14))],
            [sg.Button('Voltar')]
        ]

        single_report_window = sg.Window('Dados usuário').Layout(layout)
        button, values = self.open(single_report_window)
        single_report_window.Close()

    def show_complete_report(self, messages: list):
        layout = [
            [sg.Text(f'Relatórios', font=("Helvica", 25))]
        ]

        for message in messages:
            layout.append([sg.Text(message, size=(100, 1))])

        layout.append([sg.Cancel('Voltar')])

        user_data_window = sg.Window('Dados Curso').Layout(layout)
        button, values = self.open(user_data_window)

        user_data_window.Close()

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
