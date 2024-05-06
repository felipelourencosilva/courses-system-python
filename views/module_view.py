from views.abstract_view import AbstractView


class ModuleView(AbstractView):

    def __init__(self):
        pass

    def view_options(self):
        options = {
            1: "Adicionar Módulo",
            2: "Remover Módulo",
            3: "Editar Módulo",
            4: "Listar Módulos",
            5: "Ir para tela de Aulas",
            0: "Voltar"
        }
        return super().view_options("MÓDULOS", options)

    def get_add_module_data(self):
        data = dict()
        data["title"] = self.read_with_n_chars("Título: ", "Título do módulo deve ter pelo menos 4 letras.", 4)
        data["description"] = input("Descrição: ")
        return data

    def get_edit_module_data(self):
        self.print_title("DADOS MÓDULO")
        data = dict()
        data["title"] = self.read_with_n_chars("Título: ", "Título do módulo deve ter pelo menos 4 letras.", 4)
        data["description"] = input("Descrição: ")
        return data

    def show_module(self, module_data):
        print("Título do módulo: ", module_data["title"])
        print("Descrição do módulo: ", module_data["description"])
        print("Id: ", module_data["id"])
        print()

    def read_course_id(self):
        return self.read_int_range(
            "Digite o ID do curso: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )

    def read_module_id(self):
        return self.read_int_range(
            "Digite o ID do modulo: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )
