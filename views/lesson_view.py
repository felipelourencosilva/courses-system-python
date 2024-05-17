from views.abstract_view import AbstractView
from rich.console import Console
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
        print("Título da aula:", lesson_data["title"])
        print("Descrição da aula:", lesson_data["description"])
        print("Id:", lesson_data["id"])
        video_url = lesson_data["video_url"]
        console.print("Url do vídeo", style="link " + str(video_url) + " #")
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
