import re


class ProducerView:

    def view_options(self):
        print("-------- PRODUTOR --------")
        print("Escolha alguma opção:")
        print("1 - Adicionar Produtor")
        print("2 - Excluir Produtor")
        print("3 - Editar Produtor")
        print("4 - Listar Produtores")
        print("0 - Voltar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 5):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)

    def get_add_producer_data(self):
        data = self.get_edit_producer_data()
        cpf = input("CPF: ")
        while not cpf.isnumeric() or int(cpf) <= 0:
            print("O CPF deve ser um inteiro maior que 0.")
            cpf = input("CPF: ")
        data["cpf"] = int(cpf)
        return data

    def get_edit_producer_data(self):
        print("-------- DADOS PRODUTOR --------")
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

    def show_producer(self, user_data):
        print("Nome do usuário: ", user_data["name"])
        print("Email do usuário: ", user_data["email"])
        print("Senha do usuário: ", user_data["password"])
        print("CPF do usuário: ", user_data["cpf"])
        print()

    def read_cpf(self):
        while True:
            cpf = input("Digite o CPF do produtor: ")
            if not cpf.isnumeric() or int(cpf) <= 0:
                print("O CPF precisa ser um inteiro maior que 0")
                continue
            return int(cpf)

    def show_message(self, msg):
        print(msg)
