from views.abstract_view import AbstractView


class SystemView(AbstractView):

    def __init__(self):
        pass

    def view_options(self) -> int:
        options = {
            1: "Ir para tela de Usuário",
            2: "Ir para tela de Produtor",
            3: "Ir para tela de Afiliado",
            4: "Ir para tela de Cursos",
            5: "Ir para tela de Relatórios",
            0: "Sair"
        }
        return super().view_options("SISTEMA DE CURSOS", options)
