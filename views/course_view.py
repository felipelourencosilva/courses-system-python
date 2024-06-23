from views.abstract_view import AbstractView
import PySimpleGUI as sg
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()


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
            [sg.Text('CPF do Produtor:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        user_data_window = sg.Window('Dados Curso').Layout(layout)
        button, values = self.open(user_data_window)

        user_data_window.Close()
        return values

    def show_courses(self, courses_data):
        layout = [
            [sg.Text(f'Cursos: ', font=("Helvica", 25))],
        ]



        for course in courses_data:
            layout.extend([
                [sg.Text(f'Nome: {course["name"]}', size=(60, 1))],
                [sg.Text(f'Descrição: {course["description"]}', size=(60, 1))],
                [sg.Text(f'Preço: {course["price"]}', size=(60, 1))],
                [sg.Text(f'ID: {course["id"]}', size=(60, 1))],
                [sg.Text(f'Produtor: {course["producer"]}', size=(60, 1))],
                [sg.Text('----------------------------------------', size=(60, 1))]
            ])

        layout.append([sg.Button('Confirmar'), sg.Cancel('Voltar')])
        show_courses_window = sg.Window('Cursos').Layout(layout)
        button, values = self.open(show_courses_window)
        show_courses_window.Close()

    def read_id(self):
        return self.read_int_range(
            "Digite o ID do curso: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )
