from views.abstract_view import AbstractView


class LessonView(AbstractView):

    def __init__(self):
        pass

    def view_options(self):
        options = {
            1: "Adicionar Aula",
            2: "Remover Aula",
            3: "Editar Aula",
            4: "Listar Aulas",
            0: "Voltar"
        }
        return super().view_options("AULAS", options)
