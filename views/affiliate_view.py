from views.abstract_view import AbstractView


class AffiliateView(AbstractView):

    def __init__(self):
        pass
    def view_options(self) -> int:
        options = {
            1: "Adicionar Afiliado",
            2: "Excluir Afiliado",
            3: "Editar Afiliado",
            4: "Listar Afiliados",
            0: "Voltar"
        }
        return super().view_options("AFILIADO", options)

    def get_edit_affiliate_data(self):
        return super().read_basic_edit_user_data("AFILIADO")

    def show_affiliate(self, affiliate_data):
        print("Nome do afiliado: ", affiliate_data["name"])
        print("Email do afiliado: ", affiliate_data["email"])
        print("Senha do afiliado: ", affiliate_data["password"])
        print("CPF do afiliado: ", affiliate_data["cpf"])
        print("Saldo do afiliado: ", affiliate_data["balance"])
        print()
