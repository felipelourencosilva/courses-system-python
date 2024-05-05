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
        print("-------- DADOS AFILIADO --------")
        name = input("Nome: ")
        surname = input("Sobrenome: ")
        email = input("Email: ")
        password = input("Senha: ")
        cpf = int(input("CPF: "))

        return {"name": name, "surname": surname, "email": email,
                "password": password, "cpf": cpf}

    def get_edit_affiliate_data(self):
        print("-------- DADOS AFILIADO --------")
        name = input("Nome: ")
        surname = input("Sobrenome: ")
        email = input("Email: ")
        password = input("Senha: ")

        return {"name": name, "surname": surname, "email": email,
                "password": password}

    def show_affiliate(self, affiliate_data):
        print("Nome do afiliado: ", affiliate_data["name"])
        print("Email do afiliado: ", affiliate_data["email"])
        print("Senha do afiliado: ", affiliate_data["password"])
        print("CPF do afiliado: ", affiliate_data["cpf"])
        print()

    def read_cpf(self):
        while True:
            cpf = input("Digite o CPF do afiliado: ")
            if not cpf.isnumeric() or int(cpf) <= 0:
                print("O CPF precisa ser um inteiro maior que 0")
                continue
            return int(cpf)

    def show_message(self, msg):
        print(msg)
