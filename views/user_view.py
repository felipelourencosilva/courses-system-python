from views.abstract_view import AbstractView


class UserView(AbstractView):

    def __init__(self):
        pass

    def view_options(self):
        options = {
            1: "Adicionar Usuário",
            2: "Excluir Usuário",
            3: "Editar Usuário",
            4: "Listar Usuários",
            5: "Adicionar saldo ao Usuário",
            0: "Voltar"
        }
        return super().view_options("USUÁRIO", options)

    def get_edit_user_data(self):
        return super().read_basic_edit_user_data("USUÁRIO")

    def show_user(self, user_data):
        print("Nome do usuário: ", user_data["name"])
        print("Email do usuário: ", user_data["email"])
        print("Senha do usuário: ", user_data["password"])
        print("CPF do usuário: ", user_data["cpf"])
        print("Saldo do usuário: ", user_data["balance"])
        print("Cursos do usuário: ", end="")
        if len(user_data["courses"]) == 0:
            print("Nenhum")
        else:
            print(*user_data["courses"], sep = ", ")
        print()
