from views.abstract_view import AbstractView


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
