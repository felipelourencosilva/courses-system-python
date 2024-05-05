import re


class CourseView:

    def view_options(self):
        print("-------- CURSOS --------")
        print("Escolha alguma opção:")
        print("1 - Adicionar Curso")
        print("2 - Editar Curso")
        print("3 - Listar Cursos")
        print("4 - Comprar Curso")
        print("0 - Voltar")

        while True:
            option = input("Sua escolha: ")
            if not option.isnumeric() or int(option) not in range(0, 5):
                print("Por favor, escolha um número dentre as opções.")
                continue
            return int(option)

    def get_add_course_data(self):
        data = self.get_edit_course_data()

        cpf = input("CPF do Produtor: ")
        while not cpf.isnumeric() or int(cpf) <= 0:
            print("O CPF deve ser um inteiro maior que 0.")
            cpf = input("CPF: ")
        data["cpf"] = int(cpf)
        return data

    def get_edit_course_data(self):
        print("-------- DADOS CURSO --------")
        data = {}

        name = input("Nome: ")
        while len(name) < 4:
            print("Nome do curso deve ter pelo menos 4 letras.")
            name = input("Nome: ")
        data["name"] = name

        data["description"] = input("Descrição: ")

        price = input("Preço: ")
        isDecimal = bool(re.search(r"\d*\.\d+", price))
        while ((not price.isnumeric()) and (not isDecimal)):
            print("Preço deve ser um número decimal separado por '.'.")
            price = input("Preço: ")
            isDecimal = bool(re.search(r"\d*\.\d+", price))
        data["price"] = float(price)

        commission_percentage = input("Porcentagem da comissão (Ex: 15, 25, 50): ")
        while not commission_percentage.isnumeric() or int(commission_percentage) < 0 or int(commission_percentage) > 100:
            print("Porcentagem da comissão deve ser um número inteiro positivo entre 0 e 100.")
            commission_percentage = input("Porcentagem da comissão (Ex: 15, 25, 50): ")
        data["commission_percentage"] = int(commission_percentage)

        return data

    def show_course(self, course_data):
        print("Nome do curso: ", course_data["name"])
        print("Descrição do curso: ", course_data["description"])
        print("Preço: ", course_data["price"])
        print("Id: ", course_data["id"])
        print()

    def read_id(self):
        while True:
            id = input("Digite o ID do curso: ")
            if not id.isnumeric() or int(id) <= 0 or int(id) > 1000:
                print("O ID precisa ser um inteiro maior que 0")
                continue
            return int(id)

    def read_cpf(self):
        while True:
            cpf = input("Digite o CPF do usuário: ")
            if not cpf.isnumeric() or int(cpf) <= 0:
                print("O CPF precisa ser um inteiro maior que 0")
                continue
            return int(cpf)

    def show_message(self, msg):
        print(msg)
