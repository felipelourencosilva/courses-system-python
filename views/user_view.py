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

    def get_add_user_data(self):
        return super().read_basic_add_user_data("USUÁRIO")

    def get_edit_user_data(self, user_info):
        return super().read_basic_edit_user_data("USUÁRIO", user_info)

    def show_users(self, users_data):
        headings = ["Nome", "Email", "Senha", "CPF", "Saldo", "Cursos"]
        layout = [[sg.Table(values=users_data, headings=headings, max_col_width=25, background_color='#0F0E10',
                            auto_size_columns=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='#1C2C30',
                            key='user',
                            select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
                  [sg.Button('Confirmar'), sg.Button('Voltar')]]

        show_users_window = sg.Window('Usuários').Layout(layout)
        button, values = self.open(show_users_window)
        show_users_window.Close()
        if button in (None, 'Voltar'):
            return

        selected_rows = values["user"]
        if len(selected_rows) == 0:
            return None  # no selected User
        user_row = values["user"][0]
        user_cpf = users_data[user_row][3]  # because 3rd position is the cpf
        return user_cpf

    def open(self, window):
        button, values = window.Read()
        return button, values
