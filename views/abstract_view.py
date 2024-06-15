from abc import ABC, abstractmethod
import re
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()
import PySimpleGUI as sg
from exceptions import NegativeMoneyException, WrongInputException


class AbstractView(ABC):

    @abstractmethod
    def __init__(self):
        self.__window = None
        self.__user_window = None
        self.init_components()

    def view_options(self, title: str, options: dict):
        self.init_components(title, options)
        button, values = self.__window.Read()
        opcao = 0

        for i in range(1, len(options)):
            if values[str(i)]:
                opcao = i
                break

        if button in (None, 'Cancelar'):
            opcao = 0

        self.close()

        return opcao

        while True:
            option = self.read_int(
                "Sua escolha: ",
                "Por favor, escolha um número dentre as opções."
            )
            if option not in options:
                self.show_message("Por favor, escolha um número dentre as opções.")
                continue
            return option

    def show_message(self, msg: str):
        table = Table(box=box.ROUNDED, border_style="#FF6961")
        table.add_column("Importante", justify="center", style="#FF6961")
        table.add_row(msg)

        print()
        console.print(table)
        print()

    def show_success_message(self, msg: str):
        table = Table(box=box.ROUNDED, border_style="#4FBF26")
        table.add_column("Sucesso", justify="center", style="#4FBF26")
        table.add_row(msg)

        print()
        console.print(table)
        print()

    def read_int(self, default_msg: str, error_msg: str):
        while True:
            num = input(default_msg)
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

    def read_float(self, default_msg: str, error_msg: str):
        while True:
            num = input(default_msg)
            if not num.isnumeric() and not re.search(r"\d*\.\d+", num):
                self.show_message(error_msg)
            else:
                return float(num)

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
                    raise WrongInputException
                return email
            except WrongInputException:
                self.show_message(error_msg)


    def read_with_n_chars(self, default_msg: str, error_msg: str, n: int):
        while True:
            str = input(default_msg)
            if len(str) < n:
                self.show_message(error_msg)
            else:
                return str

    def read_cpf(self, default_msg: str = None, error_msg: str = None):
        if default_msg is None:
            default_msg = "CPF: "
        if error_msg is None:
            error_msg = "O CPF deve ser um inteiro maior que 0."
        while True:
            cpf = self.read_int(default_msg, error_msg)
            if (cpf <= 0):
                self.show_message(error_msg)
            else:
                return cpf

    def print_title(self, title: str):
        console.print("\n             " + title, style="#54cdc1")

    def read_basic_edit_user_data(self, title: str):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(f'DADOS {title}', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='name')],
            [sg.Text('Sobrenome:', size=(15, 1)), sg.InputText('', key='surname')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Senha:', size=(15, 1)), sg.InputText('', key='password')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Dados usuário').Layout(layout)

        button, values = self.open()
        name = values['name']
        surname = values['surname']
        email = values['email']
        cpf = values['cpf']
        password = values['password']

        self.close()
        return {"name": name, "surname": surname, "cpf": int(cpf), "email": email, "password": password}

    def read_value(self, default_msg: str, error_msg: str):
        while True:
            value = self.read_float(default_msg, error_msg)
            try:
                if value <= 0:
                    raise NegativeMoneyException
                return value
            except NegativeMoneyException:
                self.show_message(error_msg)

    def init_components(self, title, options):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('LightGray1')
        layout = [
            [sg.Text(title, font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))]
        ]

        for k, value in sorted(options.items()):
            if k != 0:
                layout.append([sg.Radio(value,"RD1", key=str(k))])

        layout.append([sg.Button('Confirmar'), sg.Cancel('Voltar')])
        self.__window = sg.Window('Sistema de livros').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values