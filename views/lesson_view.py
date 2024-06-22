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
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar módulo').Layout(layout)

        button, values = self.open(edit_module_window)
        title = values['title']
        description = values['description']
        video_url = values['video_url']
        edit_module_window.Close()

        return {"title": title, "description": description, "video_url": video_url}

    def show_lessons(self, lessons, module_name):
        layout = [
            [sg.Text(f'Aulas do módulo {module_name}: ', font=("Helvica", 25))],
        ]

        for lesson in lessons:
            layout.extend(
                [[sg.Text(f'Título: {lesson["title"]}', size=(60, 1))],
                 [sg.Text(f'Descrição: {lesson["description"]}', size=(60, 1))],
                 [sg.Text(f'Id: {lesson["id"]}', size=(60, 1))],
                 [sg.Text(f'URL do vídeo: {lesson["video_url"]}', size=(60, 1))],
                 [sg.Text('----------------------------------------', size=(60, 1))]]
            )

        layout.append([sg.Button('Confirmar')])
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
