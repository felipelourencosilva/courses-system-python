from views.abstract_view import AbstractView
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()


class SystemView(AbstractView):

    def __init__(self):
        pass

    def show_easter_egg(self):

        art2 = '''
██╗   ██╗ ██████╗ ██╗  ████████╗███████╗    ███████╗███████╗███╗   ███╗██████╗ ██████╗ ███████╗██╗
██║   ██║██╔═══██╗██║  ╚══██╔══╝██╔════╝    ██╔════╝██╔════╝████╗ ████║██╔══██╗██╔══██╗██╔════╝██║
██║   ██║██║   ██║██║     ██║   █████╗      ███████╗█████╗  ██╔████╔██║██████╔╝██████╔╝█████╗  ██║
╚██╗ ██╔╝██║   ██║██║     ██║   ██╔══╝      ╚════██║██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══██╗██╔══╝  ╚═╝
 ╚████╔╝ ╚██████╔╝███████╗██║   ███████╗    ███████║███████╗██║ ╚═╝ ██║██║     ██║  ██║███████╗██╗
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝   ╚══════╝    ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝
        '''
        console.print(art2, style="#54cdc1")

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
