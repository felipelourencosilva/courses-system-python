from abc import ABC, abstractmethod
import re


class AbstractView(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def view_options(self, title: str, options: dict):
        self.print_title(title)
        for k, v in sorted(options.items()):
            if (k != 0):
                print(f"{k} - {v}")
        if 0 in options:
            print(f"0 - {options[0]}")

        while True:
            option = self.read_int(
                "Sua escolha: ",
                "Por favor, escolha um número dentre as opções."
            )
            if option not in options:
                print("Por favor, escolha um número dentre as opções.")
                continue
            return option

    def show_message(self, msg: str):
        print(msg)

    def read_int(self, default_msg: str, error_msg: str):
        while True:
            num = input(default_msg)
            if not num.isnumeric():
                print(error_msg)
            else:
                return int(num)

    def read_int_range(self, default_msg: str, error_msg: str, min: int, max: int):
        while True:
            num = self.read_int(default_msg, error_msg)
            if num < min or num > max:
                print(error_msg)
            else:
                return num

    def read_float(self, default_msg: str, error_msg: str):
        while True:
            num = input(default_msg)
            if not num.isnumeric() and not re.search(r"\d*\.\d+", num):
                print(error_msg)
            else:
                return float(num)

    def read_letters_string(self, default_msg: str, error_msg: str):
        while True:
            str = input(default_msg)
            if not re.search("^[^0-9!@#$%&*]*$", str):
                print(error_msg)
            else:
                return str

    def read_email(self,  default_msg: str, error_msg: str):
        while True:
            email = input(default_msg)
            if "@" not in email:
                print(error_msg)
            else:
                return email

    def read_with_n_chars(self, default_msg: str, error_msg: str, n: int):
        while True:
            str = input(default_msg)
            if len(str) < n:
                print(error_msg)
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
        print(f"-------- {title} --------")

    def read_basic_edit_user_data(self, title: str):
        data = {}
        self.print_title(title)
        while True:
            name = self.read_letters_string("Nome: ", "Nome deve conter somente letras.")
            if not name.strip():
                print("Nome deve conter somente letras.")
            else:
                data["name"] = name
                break

        data["surname"] = self.read_letters_string("Sobrenome: ", "Sobrenome deve conter somente letras.")
        data["email"] = self.read_email("Email: ", "Email deve conter '@'.")
        data["password"] = self.read_with_n_chars("Senha: ", "A senha deve ter pelo menos 4 caracteres.", 4)

        return data

    def read_basic_add_user_data(self, title: str):
        data = self.read_basic_edit_user_data(title)
        data["cpf"] = self.read_cpf()
        return data

    def read_value(self, default_msg: str, error_msg: str):
        while True:
            value = self.read_float(default_msg, error_msg)
            if value <= 0:
                print(error_msg)
            else:
                return value