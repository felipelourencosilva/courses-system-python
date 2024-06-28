from abc import ABC, abstractmethod
import re
import PySimpleGUI as sg
from exceptions import negative_value_exception, wrong_input_exception
from exceptions.wrong_input_exception import WrongInputException


class AbstractView(ABC):

    @abstractmethod
    def __init__(self):
        self.init_components()

    def view_options(self, title: str, options: dict):
        window = self.init_components(title, options)
        button, values = window.Read()
        option = 0

        for i in range(1, len(options)):
            if values[str(i)]:
                option = i
                break

        if button in (None, 'Voltar'):
            option = 0

        window.Close()
        return option

    def show_message(self, msg: str):
        sg.ChangeLookAndFeel('DarkRed2')
        layout = [
            [sg.Text('Importante:', font=("Helvica", 25))],
            [sg.Text(msg, size=(40, 1))],
            [sg.Button('Ok')]
        ]
        message_window = sg.Window('Mensagem').Layout(layout)
        button, values = self.open(message_window)
        message_window.Close()

    def show_success_message(self, msg: str):
        sg.ChangeLookAndFeel('LightGreen6')
        layout = [
            [sg.Text('Sucesso:', font=("Helvica", 25))],
            [sg.Text(msg, size=(40, 1))],
            [sg.Button('Ok')]
        ]
        success_message_window = sg.Window('Mensagem').Layout(layout)
        button, values = self.open(success_message_window)
        success_message_window.Close()

    def read_int(self, default_msg: str, error_msg: str):
        layout = [
            [sg.Text(f'{default_msg}', font=("Helvica", 25))],
            [sg.InputText('', key='int')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        read_int_window = sg.Window('Dados usuário').Layout(layout)

        button, values = self.open(read_int_window)
        num = values['int']
        read_int_window.Close()

        if not num.isnumeric():
            self.show_message(error_msg)
        else:
            return int(num)

    def read_int_range(self, default_msg: str, error_msg: str, min: int, max: int):
        while True:
            num = self.read_int(default_msg, error_msg)
            if num < min or num > max:
                self.show_message(error_msg)
            else:
                return num

    def read_float(self, default_msg: str):
        layout = [
            [sg.Text(f'{default_msg}', font=("Helvica", 25))],
            [sg.InputText('', key='float')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        read_int_window = sg.Window(default_msg).Layout(layout)

        button, values = self.open(read_int_window)
        read_int_window.Close()

        if button in (None, 'Cancelar'):
            return

        return values['float']

    def read_letters_string(self, default_msg: str, error_msg: str):
        while True:
            str = input(default_msg)
            if not re.search("^[^0-9!@#$%&*]*$", str):
                self.show_message(error_msg)
            else:
                return str

    def read_email(self,  default_msg: str, error_msg: str):
        while True:
            email = input(default_msg)
            try:
                if "@" not in email or ".com" in email:
                    raise WrongInputException()
                return email
            except WrongInputException():
                self.show_message(error_msg)

    def read_cpf(self, default_msg: str = None, error_msg: str = None):
        layout = [
            [sg.Text(f'{default_msg}', font=("Helvica", 25))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        cpf_window = sg.Window('Dados usuário').Layout(layout)

        button, values = self.open(cpf_window)
        cpf_window.Close()
        if button in (None, 'Cancelar'):
            return
        return int(values['cpf'])

    def read_basic_add_user_data(self, title: str):
        layout = [
            [sg.Text(f'DADOS {title}', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='name')],
            [sg.Text('Sobrenome:', size=(15, 1)), sg.InputText('', key='surname')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', key='password')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        user_data_window = sg.Window('Dados usuário', layout)
        button, values = self.open(user_data_window)
        user_data_window.Close()
        if button in (None, 'Voltar'):
            return
        return values

    def read_basic_edit_user_data(self, title: str):
        layout = [
            [sg.Text(f'DADOS {title}', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='name')],
            [sg.Text('Sobrenome:', size=(15, 1)), sg.InputText('', key='surname')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', key='password')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        user_data_window = sg.Window('Dados usuário').Layout(layout)

        button, values = self.open(user_data_window)
        user_data_window.Close()
        if button in (None, 'Voltar'):
            return
        return values

    def read_value(self, default_msg: str):
        return self.read_float(default_msg)

    def init_components(self, title, options):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGrey15')
        layout = [
            [sg.Text(title, font=("Helvetica", 18))],
            [sg.Text('Escolha sua opção', font=("Arial", 14))]
        ]

        for k, value in sorted(options.items()):
            if k != 0:
                layout.append([sg.Radio(value, "RD1", key=str(k))])

        layout.append([sg.Button('Confirmar'), sg.Cancel('Voltar')])
        return sg.Window('Sistema de cursos', layout)

    def open(self, window):
        button, values = window.Read()
        return button, values
