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

    def get_edit_affiliate_data(self):
        return super().read_basic_edit_user_data("AFILIADO")

    def show_comment(self, comment):
        print(comment)
        print()
