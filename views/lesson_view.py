from views.abstract_view import AbstractView
import PySimpleGUI as sg


class LessonView(AbstractView):

    def __init__(self):
        pass

    def view_options(self):
        options = {
            1: "Adicionar Aula",
            2: "Remover Aula",
            3: "Editar Aula",
            4: "Listar Aulas",
            5: "Ir para tela de Comentários",
            0: "Voltar"
        }
        return super().view_options("AULAS", options)

    def get_lesson_data(self):
        layout = [
            [sg.Text(f'Criar aula:', font=("Helvica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='title')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='description')],
            [sg.Text('Url do vídeo:', size=(15, 1)), sg.InputText('', key='video_url')],
            [sg.Text('Id do módulo:', size=(15, 1)), sg.InputText('', key='module_id')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar módulo').Layout(layout)

        button, values = self.open(edit_module_window)
        title = values['title']
        description = values['description']
        video_url = values['video_url']
        module_id = values['module_id']
        edit_module_window.Close()

        return {"title": title, "description": description, "video_url": video_url, "module_id": module_id}

    def get_edit_lesson_data(self):
        layout = [
            [sg.Text(f'Atualizar aula:', font=("Helvica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='title')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='description')],
            [sg.Text('Url do vídeo:', size=(15, 1)), sg.InputText('', key='video_url')],
            [sg.Text('Id da aula:', size=(15, 1)), sg.InputText('', key='lesson_id')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar módulo').Layout(layout)

        button, values = self.open(edit_module_window)
        title = values['title']
        description = values['description']
        video_url = values['video_url']
        lesson_id = values['lesson_id']
        edit_module_window.Close()

        return {"title": title, "description": description, "video_url": video_url, "lesson_id": lesson_id}

    def show_lessons(self, lessons):
        headings = ["Título", "Descrição", "Id", "Url do vídeo"]
        layout = [[sg.Table(values=lessons, headings=headings, max_col_width=25, background_color='lightblue',
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='lightyellow',
                            key='-TABLE-')],
                  [sg.Button('Voltar')]]

        show_users_window = sg.Window('Aulas').Layout(layout)
        button, values = self.open(show_users_window)

        show_users_window.Close()

    def read_lesson_id(self):
        return self.read_int_range(
            "Digite o ID da aula: ",
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
