from views.abstract_view import AbstractView


class SaleView(AbstractView):

    def __init__(self):
        pass

    def view_options(self) -> int:
        options = {
            1: "Gerar relatório completo",
            2: "Mostrar Curso mais vendido",
            3: "Mostrar Curso com maior lucro",
            4: "Mostrar Usuário com mais cursos",
            5: "Mostrar Produtor com mais vendas",
            6: "Mostrar Produtor com maior lucro",
            7: "Mostrar Afiliado com mais vendas",
            8: "Mostrar Afiliado com maior lucro",
            0: "Voltar"
        }
        return super().view_options("RELATÓRIOS", options)
