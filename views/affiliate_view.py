import re


class AffiliateView:

    def view_options(self) -> int:
        print("-------- AFILIADO --------")
        print("Escolha alguma opção:")
        print("1 - Adicionar Afiliado")
        print("2 - Excluir Afiliado")
        print("3 - Editar Afiliado")
        print("4 - Listar Afiliados")
        print("0 - Voltar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 5):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)

    def get_add_affiliate_data(self):
        data = self.get_edit_affiliate_data()
        cpf = input("CPF: ")
        while not cpf.isnumeric() or int(cpf) <= 0:
            print("O CPF deve ser um inteiro maior que 0.")
            cpf = input("CPF: ")
        data["cpf"] = int(cpf)
        return data

    def get_edit_affiliate_data(self):
        print("-------- DADOS AFILIADO --------")
        name = input("Nome: ")
        while not (re.search("^[a-zA-Z ]*$", name) and name.strip()):
            print("Nome deve conter somente letras.")
            name = input("Nome: ")
            valid = re.search("^[a-zA-Z ]*$", name) and name.strip()

        surname = input("Sobrenome: ")
        while not re.search("^[a-zA-Z ]*$", surname):
            print("Sobrenome deve conter somente letras.")
            surname = input("Sobrenome: ")

        email = input("Email: ")
        while "@" not in email:
            print("Email deve conter '@'.")
            email = input("Email: ")

        password = input("Senha: ")
        while len(password) < 4:
            print("A senha deve ter pelo menos 4 caracteres.")
            password = input("Senha: ")

        return {"name": name, "surname": surname, "email": email,
                "password": password}

    def show_affiliate(self, affiliate_data):
        print("Nome do afiliado: ", affiliate_data["name"])
        print("Email do afiliado: ", affiliate_data["email"])
        print("Senha do afiliado: ", affiliate_data["password"])
        print("CPF do afiliado: ", affiliate_data["cpf"])
        print("Saldo do afiliado: ", affiliate_data["balance"])
        print()

    def read_cpf(self):
        while True:
            cpf = input("Digite o CPF do afiliado: ")
            if not cpf.isnumeric() or int(cpf) <= 0:
                print("O CPF precisa ser um inteiro maior que 0")
                continue
            return int(cpf)

    def read_value(self):
        while True:
            value = input("Digite o valor que deseja adicionar: ")
            if float(value) <= 0:
                print("O valor precisa ser um inteiro maior que 0")
                continue
            return float(value)

    def show_message(self, msg):
        print(msg)
