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

    def get_edit_course_data(self):
        self.print_title("DADOS CURSO")
        data = {}
        data["name"] = self.read_with_n_chars("Nome: ", "Nome do curso deve ter pelo menos 4 letras.", 4)
        data["description"] = input("Descrição: ")
        data["price"] = self.read_value("Preço: ", "Preço deve ser um número decimal separado por '.'.")

        data["commission_percentage"] = self.read_int_range(
            "Porcentagem da comissão (Ex: 15, 25, 50): ",
            "Porcentagem da comissão deve ser um número inteiro positivo entre 0 e 100.",
            0,
            100
        )
        return data

    def show_course(self, course_data):
        print("Nome do curso: ", course_data["name"])
        print("Descrição do curso: ", course_data["description"])
        print("Preço: ", course_data["price"])
        print("Id: ", course_data["id"])
        print()

    def read_id(self):
        return self.read_int_range(
            "Digite o ID do curso: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )
