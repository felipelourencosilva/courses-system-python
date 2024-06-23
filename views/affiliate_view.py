from views.abstract_view import AbstractView
import PySimpleGUI as sg

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
        return super().view_options("AFILIADOS", options)

    def get_edit_affiliate_data(self):
        return super().read_basic_edit_user_data("AFILIADO")

    def show_affiliates(self, affiliates):
        headings = ["Nome", "Email", "CPF", "Senha", "Saldo"]
        layout = [[sg.Table(values=affiliates, headings=headings, max_col_width=25, background_color='lightblue',
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='lightyellow',
                            key='-TABLE-')],
                  [sg.Button('Voltar')]]

        show_users_window = sg.Window('Afiliados').Layout(layout)
        button, values = self.open(show_users_window)

        show_users_window.Close()

    def open(self, window):
        button, values = window.Read()
        return button, values
