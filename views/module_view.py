from views.abstract_view import AbstractView
import PySimpleGUI as sg


class ModuleView(AbstractView):

    def __init__(self):
        pass

    def view_options(self):
        options = {
            1: "Adicionar Módulo",
            2: "Remover Módulo",
            3: "Editar Módulo",
            4: "Listar Módulos",
            5: "Ir para tela de Aulas",
            0: "Voltar"
        }
        return super().view_options("MÓDULOS", options)

    def get_add_module_data(self):
        layout = [
            [sg.Text(f'Criar módulo', font=("Helvica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='title')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='description')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar módulo').Layout(layout)
        button, values = self.open(edit_module_window)
        edit_module_window.Close()

        if button in (None, 'Voltar'):
            return
        return values

    def get_edit_module_data(self, info):
        layout = [
            [sg.Text(f'Criar módulo', font=("Helvica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText(info["title"], key='title')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText(info["description"], key='description')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar módulo').Layout(layout)
        button, values = self.open(edit_module_window)
        edit_module_window.Close()

        if button in (None, 'Voltar'):
            return
        return values

    def show_modules(self, module_data):
        headings = ["Título", "Descição", "Id"]
        layout = [[sg.Table(values=module_data, headings=headings, max_col_width=25, background_color='#0F0E10',
                            auto_size_columns=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='#1C2C30',
                            key='module',
                            select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
                  [sg.Button('Confirmar'), sg.Button('Voltar')]]

        show_modules_window = sg.Window('Modulos').Layout(layout)
        button, values = self.open(show_modules_window)
        show_modules_window.Close()

        if button in (None, 'Voltar'):
            return None

        selected_rows = values["module"]
        if len(selected_rows) == 0:
            return None  # no selected Module
        module_row = values["module"][0]
        module_id = module_data[module_row][2]  # because 2nd position is the id
        return int(module_id)

    def read_course_id(self):
        return self.read_int_range(
            "Digite o ID do curso: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )

    def read_module_id(self):
        return self.read_int_range(
            "Digite o ID do módulo: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )

    def open(self, window):
        button, values = window.Read()
        return button, values
