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

    def get_add_affiliate_data(self):
        return super().read_basic_add_user_data("AFILIADO")

    def get_edit_affiliate_data(self):
        return super().read_basic_edit_user_data("AFILIADO")

    def show_affiliates(self, affiliate_data, show_no_affiliate_button):
        headings = ["Nome", "Email", "Senha", "CPF", "Saldo"]
        button_list = [sg.Button('Confirmar'), sg.Button('Voltar')]
        if show_no_affiliate_button:
            button_list.append(sg.Button('Sem Afiliado'))
        layout = [[sg.Table(values=affiliate_data, headings=headings, max_col_width=25, background_color='#0F0E10',
                            auto_size_columns=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='#1C2C30',
                            key='affiliate',
                            select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
                  button_list]

        show_affiliates_window = sg.Window('Afiliados').Layout(layout)
        button, values = self.open(show_affiliates_window)
        show_affiliates_window.Close()
        if button in (None, 'Voltar'):
            return
        if button == 'Sem Afiliado':
            return -1

        selected_rows = values["affiliate"]
        if len(selected_rows) == 0:
            return None  # no selected Affiliate
        affiliate_row = values["affiliate"][0]
        affiliate_cpf = affiliate_data[affiliate_row][3]  # because 3rd position is the cpf
        return affiliate_cpf

    def open(self, window):
        button, values = window.Read()
        return button, values
