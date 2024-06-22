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
        layout = [
            [sg.Text(f'Afiliados: ', font=("Helvica", 25))],
        ]

        for affiliate in affiliates:
            layout.extend(
                [[sg.Text(f'Nome: {affiliate["name"]}', size=(60, 1))],
                 [sg.Text(f'Email: {affiliate["email"]}', size=(60, 1))],
                 [sg.Text(f'CPF: {affiliate["cpf"]}', size=(60, 1))],
                 [sg.Text(f'Senha: {affiliate["password"]}', size=(60, 1))],
                 [sg.Text(f'Saldo: {affiliate["balance"]}', size=(60, 1))],
                 [sg.Text('----------------------------------------', size=(60, 1))]]
            )

        layout.append([sg.Cancel('Voltar')])
        show_affiliates_window = sg.Window('Afiliados').Layout(layout)
        button, values = self.open(show_affiliates_window)

        show_affiliates_window.Close()

    def open(self, window):
        button, values = window.Read()
        return button, values
