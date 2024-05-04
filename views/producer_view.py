class ProducerView:

    def view_options(self):
        print("-------- PRODUTORES ----------")
        print("Escolha a opcao")
        print("1 - Adicionar Produtores")
        print("2 - Excluir Produtores")
        print("3 - Editar Produtores")
        print("4 - Listar Produtores")
        print("0 - Retornar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 5):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)

    def get_add_producer_data(self):
        print("-------- DADOS PRODUTORES ----------")
        name = input("Nome: ")
        surname = input("Sobrenome: ")
        email = input("Email: ")
        password = input("Password: ")
        cpf = int(input("CPF: "))

        return {"name": name, "surname": surname, "email": email,
                "password": password, "cpf": cpf}

    def get_edit_producer_data(self):
        print("-------- DADOS PRODUTORES ----------")
        name = input("Nome: ")
        surname = input("Sobrenome: ")
        email = input("Email: ")
        password = input("Password: ")

        return {"name": name, "surname": surname, "email": email,
                "password": password}

    def show_producer(self, user_data):
        print("Nome do usuário: ", user_data["name"])
        print("Email do usuário: ", user_data["email"])
        print("Senha do usuário: ", user_data["password"])
        print("CPF do usuário: ", user_data["cpf"])
        print("\n")

    def read_cpf(self):
        while True:
            cpf = input("Digite o CPF do usuário: ")
            if not cpf.isnumeric or int(cpf) <= 0:
                print("O CPF precisa ser um inteiro maior que 0")
                continue
            return int(cpf)

    def show_message(self, msg):
        print(msg)
