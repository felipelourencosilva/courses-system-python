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
        layout = [
            [sg.Text(f'Usuários: ', font=("Helvica", 25))],
        ]

        for user in users_data:
            layout.extend(
                [[sg.Text(f'Nome: {user["name"]}', size=(60, 1))],
                 [sg.Text(f'Email: {user["email"]}', size=(60, 1))],
                 [sg.Text(f'CPF: {user["cpf"]}', size=(60, 1))],
                 [sg.Text(f'Senha: {user["password"]}', size=(60, 1))],
                 [sg.Text(f'Saldo: {user["balance"]}', size=(60, 1))],]
            )

            if len(user["courses"]) == 0:
                layout.append([sg.Text(f'Cursos do usuário: Nenhum', size=(60, 1))])
            else:
                layout.append([sg.Text(f'Cursos do usuário: ' + " ".join(user["courses"]))])

            layout.append([sg.Text('----------------------------------------', size=(60, 1))])

        layout.append([sg.Button('Confirmar'), sg.Cancel('Voltar')])
        show_users_window = sg.Window('Usuarios').Layout(layout)
        button, values = self.open(show_users_window)

        show_users_window.Close()

    def open(self, window):
        button, values = window.Read()
        return button, values
