from views.abstract_view import AbstractView
import PySimpleGUI as sg


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
        return super().view_options("USUÁRIOS", options)

    def get_edit_user_data(self):
        return super().read_basic_edit_user_data("USUÁRIO")

    def show_users(self, users_data):
        headings = ["Nome", "Email", "CPF", "Senha", "Saldo"]
        layout = [[sg.Table(values=users_data, headings=headings, max_col_width=25, background_color='lightblue',
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='lightyellow',
                            key='-TABLE-')],
                  [sg.Button('Confirmar'), sg.Button('Voltar')]]

        show_users_window = sg.Window('Usuarios').Layout(layout)
        button, values = self.open(show_users_window)

        show_users_window.Close()

    def open(self, window):
        button, values = window.Read()
        return button, values
