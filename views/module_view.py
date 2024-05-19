from views.abstract_view import AbstractView
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()


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
        showModuleTable = Table(box=box.ROUNDED, border_style="#6D7280")
        showModuleTable.add_column("Módulo",justify="left", style="#54cdc1")
        showModuleTable.add_column("Informações", justify="left", style="bold italic")
        showModuleTable.add_row("Título do módulo", str(module_data["title"]))
        showModuleTable.add_row("Descrição do módulo", str(module_data["description"]))
        showModuleTable.add_row("Id", str(module_data["id"]))
        console.print(showModuleTable)
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
            "Digite o ID do módulo: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )
