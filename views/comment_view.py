from views.abstract_view import AbstractView


class CommentView(AbstractView):

    def __init__(self):
        pass

    def view_options(self) -> int:
        options = {
            1: "Adicionar Comentário",
            2: "Excluir Comentário",
            3: "Editar Comentário",
            4: "Listar Comentários",
            0: "Voltar"
        }
        return super().view_options("COMENTARIO", options)

    def get_comment_data(self):
        data = dict()
        data["comment"] = input("Comentário: ")
        return data

    def show_comment(self, comment_data):
        print("Comentário: ", comment_data["description"])
        print()

    def read_lesson_id(self):
        return self.read_int_range(
            "Digite o ID da aula: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )

    def read_comment_id(self):
        return self.read_int_range(
            "Digite o ID do comentário: ",
            "O ID precisa ser um inteiro entre 1 e 1000",
            1,
            1000
        )
