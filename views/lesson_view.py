from views.abstract_view import AbstractView
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()

class LessonView(AbstractView):

    def __init__(self):
        pass

    def view_options(self):
        options = {
            1: "Adicionar Aula",
            2: "Remover Aula",
            3: "Editar Aula",
            4: "Listar Aulas",
            5: "Ir para tela de Comentários",
            0: "Voltar"
        }
        return super().view_options("AULAS", options)

    def get_lesson_data(self):
        data = dict()
        data["title"] = self.read_with_n_chars("Título: ", "Título do módulo deve ter pelo menos 4 letras.", 4)
        data["description"] = input("Descrição: ")
        data["video_url"] = input("Url do Vídeo: ")
        return data

    def show_lesson(self, lesson_data):
        showLessonTable = Table(box=box.ROUNDED, border_style="#6D7280")
        showLessonTable.add_column("Aula", justify="left", style="#54cdc1")
        showLessonTable.add_column("Informações", justify="left", style="bold italic")
        showLessonTable.add_row("Título da aula", str(lesson_data["title"]))
        showLessonTable.add_row("Descrição da aula", str(lesson_data["description"]))
        showLessonTable.add_row("Id", str(lesson_data["id"]))
        video_url = lesson_data["video_url"]
        showLessonTable.add_row("Url do vídeo", str(video_url), style="link " + str(video_url) + " #1260CC")
        console.print(showLessonTable)
        print()

    def read_lesson_id(self):
        return self.read_int_range(
            "Digite o ID da aula: ",
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
