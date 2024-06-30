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
            [sg.Text(f'Criar aula', font=("Helvica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='title')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='description')],
            [sg.Text('Url do vídeo:', size=(15, 1)), sg.InputText('', key='video_url')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar módulo').Layout(layout)
        button, values = self.open(edit_module_window)
        edit_module_window.Close()

        if button in (None, 'Voltar'):
            return
        return values

    def get_edit_lesson_data(self, info):
        layout = [
            [sg.Text(f'Atualizar aula:', font=("Helvica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText(info["title"], key='title')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText(info["description"], key='description')],
            [sg.Text('Url do vídeo:', size=(15, 1)), sg.InputText(info["video_url"], key='video_url')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_lesson_window = sg.Window('Criar modulo').Layout(layout)
        button, values = self.open(edit_lesson_window)
        edit_lesson_window.Close()

        if button in (None, 'Voltar'):
            return
        return values

    def show_lessons(self, lesson_data):
        headings = ["Título", "Descrição", "Id", "Url do vídeo"]
        layout = [[sg.Table(values=lesson_data, headings=headings, max_col_width=25, background_color='#0F0E10',
                            auto_size_columns=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='#1C2C30',
                            key='lesson',
                            select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
                  [sg.Button('Confirmar'), sg.Button('Voltar')]]

        show_lessons_window = sg.Window('Aulas').Layout(layout)
        button, values = self.open(show_lessons_window)
        show_lessons_window.Close()

        if button in (None, 'Voltar'):
            return None

        selected_rows = values["lesson"]
        if len(selected_rows) == 0:
            return None  # no selected Lesson
        lesson_row = values["lesson"][0]
        lesson_id = lesson_data[lesson_row][2]  # because 2nd position is the id
        return int(lesson_id)
