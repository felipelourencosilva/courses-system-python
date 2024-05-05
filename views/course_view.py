from views.abstract_view import AbstractView


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

    def get_add_course_data(self):
        data = self.get_edit_course_data()

        cpf = input("CPF do Produtor: ")
        while not cpf.isnumeric() or int(cpf) <= 0:
            print("O CPF deve ser um inteiro maior que 0.")
            cpf = input("CPF: ")
        data["cpf"] = int(cpf)
        return data

    def get_edit_course_data(self):
        self.print_title("DADOS CURSO")
        data = {}
        data["name"] = self.read_with_n_chars("Nome: ", "Nome do curso deve ter pelo menos 4 letras.", 4)
        data["description"] = input("Descrição: ")
        data["price"] = self.read_value("Preço: ", "Preço deve ser um número decimal separado por '.'.")

        while True:
            commission_percentage = self.read_int("Porcentagem da comissão (Ex: 15, 25, 50): ", "Porcentagem da comissão deve ser um número inteiro positivo entre 0 e 100.")
            if (commission_percentage < 0 or commission_percentage > 100):
                print("Porcentagem da comissão deve ser um número inteiro positivo entre 0 e 100.")
            else:
                data["commission_percentage"] = commission_percentage
                break

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
            else:
                return int(id)
