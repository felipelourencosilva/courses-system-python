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
        print("-------- DADOS CURSO --------")
        name = input("Nome: ")
        description = input("Descrição: ")
        price = float(input("Preço: "))
        commission_percentage = int(input("Porcentagem da comissão (Ex: 15, 25, 50): "))
        cpf = int(input("CPF do produtor: "))

        return {"name": name, "description": description, "price": price,
                "commission_percentage": commission_percentage, "cpf": cpf}

    def get_edit_course_data(self):
        print("-------- DADOS CURSO ----------")
        name = input("Nome: ")
        description = input("Descrição: ")
        price = float(input("Preço: "))
        commission_percentage = int(input("Porcentagem da comissão (Ex: 15, 25, 50): "))

        return {"name": name, "description": description, "price": price,
                "commission_percentage": commission_percentage}

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

    def show_message(self, msg):
        print(msg)
