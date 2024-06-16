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
        layout = [
            [sg.Text(f'Produtores: ', font=("Helvica", 25))],
        ]

        for producer in producers:
            layout.extend(
                [[sg.Text(f'Nome: {producer["name"]}', size=(60, 1))],
                 [sg.Text(f'Email: {producer["email"]}', size=(60, 1))],
                 [sg.Text(f'CPF: {producer["cpf"]}', size=(60, 1))],
                 [sg.Text(f'Senha: {producer["password"]}', size=(60, 1))],
                 [sg.Text(f'Saldo: {producer["balance"]}', size=(60, 1))],
                 [sg.Text('----------------------------------------', size=(60, 1))]]
            )

        layout.append([sg.Cancel('Voltar')])
        show_producers_window = sg.Window('Produtores').Layout(layout)
        button, values = self.open(show_producers_window)

        show_producers_window.Close()

    def open(self, window):
        button, values = window.Read()
        return button, values
