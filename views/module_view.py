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
            [sg.Text('Id do curso:', size=(15, 1)), sg.InputText('', key='course_id')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar módulo').Layout(layout)

        button, values = self.open(edit_module_window)
        title = values['title']
        description = values['description']
        course_id = values['course_id']
        edit_module_window.Close()

        return {"title": title, "description": description, "course_id": course_id}

    def get_edit_module_data(self):
        layout = [
            [sg.Text(f'Criar módulo', font=("Helvica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='title')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='description')],
            [sg.Text('Id do módulo:', size=(15, 1)), sg.InputText('', key='module_id')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar módulo').Layout(layout)

        button, values = self.open(edit_module_window)
        title = values['title']
        description = values['description']
        module_id = values['module_id']
        edit_module_window.Close()

        return {"title": title, "description": description, "module_id": module_id}

    def show_modules(self, modules):
        headings = ["Título", "Descição", "Id"]
        layout = [[sg.Table(values=modules, headings=headings, max_col_width=25, background_color='lightblue',
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='lightyellow',
                            key='-TABLE-')],
                  [sg.Button('Voltar')]]

        show_users_window = sg.Window('Modulos').Layout(layout)
        button, values = self.open(show_users_window)

        show_users_window.Close()

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
