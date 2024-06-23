from views.abstract_view import AbstractView
import PySimpleGUI as sg


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

    def show_producers(self, producers):
        headings = ["Nome", "Email", "CPF", "Senha", "Saldo"]
        layout = [[sg.Table(values=producers, headings=headings, max_col_width=25, background_color='lightblue',
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='lightyellow',
                            key='-TABLE-')],
                  [sg.Button('Voltar')]]

        show_users_window = sg.Window('Produtor').Layout(layout)
        button, values = self.open(show_users_window)

        show_users_window.Close()

    def open(self, window):
        button, values = window.Read()
        return button, values
