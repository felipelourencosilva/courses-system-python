from views.abstract_view import AbstractView
import PySimpleGUI as sg


class CourseView(AbstractView):

    def __init__(self):
        pass

    def view_options(self) -> int:
        options = {
            1: "Adicionar Curso",
            2: "Editar Curso",
            3: "Listar Cursos",
            4: "Comprar Curso",
            5: "Ir para tela de Módulos",
            0: "Voltar"
        }
        return super().view_options("CURSOS", options)

    def get_edit_course_data(self):
        sg.ChangeLookAndFeel('LightGray1')
        layout = [
            [sg.Text(f'DADOS CURSO', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='name')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='description')],
            [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='price')],
            [sg.Text('Comissão:', size=(15, 1)), sg.InputText('', key='commission_percentage')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        user_data_window = sg.Window('Dados Curso').Layout(layout)
        button, values = self.open(user_data_window)

        user_data_window.Close()
        return values

    def get_add_course_data(self):
        sg.ChangeLookAndFeel('LightGray1')
        layout = [
            [sg.Text(f'DADOS CURSO', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='name')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='description')],
            [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='price')],
            [sg.Text('Comissão:', size=(15, 1)), sg.InputText('', key='commission_percentage')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        user_data_window = sg.Window('Dados Curso').Layout(layout)
        button, values = self.open(user_data_window)

        user_data_window.Close()
        return values

    def show_courses(self, course_data):
        headings = ["Nome", "Descrição", "Preço", "Id", "Produtor"]
        layout = [[sg.Table(values=course_data, headings=headings, max_col_width=25, background_color='#0F0E10',
                            auto_size_columns=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='#1C2C30',
                            key='course',
                            select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
                  [sg.Button('Confirmar'), sg.Button('Voltar')]]

        show_courses_window = sg.Window('Cursos').Layout(layout)
        button, values = self.open(show_courses_window)
        show_courses_window.Close()
        if button in (None, 'Voltar'):
            return

        selected_rows = values["course"]
        if len(selected_rows) == 0:
            return None  # no selected Course
        course_row = values["course"][0]
        course_id = course_data[course_row][3]  # because 4th position is the id
        return int(course_id)

    def read_id(self):
        return self.read_int_range(
            "Digite o ID do curso: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )
