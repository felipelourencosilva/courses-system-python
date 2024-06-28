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

    def get_add_producer_data(self):
        return super().read_basic_add_user_data("PRODUTOR")

    def get_edit_producer_data(self):
        return super().read_basic_edit_user_data("PRODUTOR")

    def show_producers(self, producer_data):
        headings = ["Nome", "Email", "Senha", "CPF", "Saldo"]
        layout = [[sg.Table(values=producer_data, headings=headings, max_col_width=25, background_color='lightblue',
                            auto_size_columns=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='lightyellow',
                            key='producer',
                            select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
                  [sg.Button('Confirmar'), sg.Button('Voltar')]]

        show_producers_window = sg.Window('Produtores').Layout(layout)
        button, values = self.open(show_producers_window)
        show_producers_window.Close()
        if button in (None, 'Voltar'):
            return

        selected_rows = values["producer"]
        if len(selected_rows) == 0:
            return None  # no selected Producer
        producer_row = values["producer"][0]
        producer_cpf = producer_data[producer_row][3]  # because 3rd position is the cpf
        return producer_cpf

    def open(self, window):
        button, values = window.Read()
        return button, values
