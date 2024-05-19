from views.abstract_view import AbstractView
from rich.console import Console
from rich import box
from rich.table import Table
console = Console()


class SystemView(AbstractView):

    def __init__(self):
        pass

    def show_easter_egg(self):
        showLessonTable = Table(box=box.ROUNDED, border_style="#EB5717")
        showLessonTable.add_column("Obrigado por utilizar SisCursos", justify="center", style="#EB5717")
        art = '''
                          _______
                         | ___  o|
                         |[_-_]_ |
      ______________     |[_____]|
     |.------------.|    |[_____]|
     ||            ||    |[====o]|
     || SISCURSOS  ||    |[_.--_]|
     || opa felipe ||    |[_____]|
     ||            ||    |      :|
     ||____________||    |      :|
 .==.|""  ......    |.==.|      :|
 |::| '-.________.-' |::||      :|
 |''|  (__________)-.|''||______:|
 `""`_.............._\\""`______
    /:::::::::::'':::\\`;'-.-.  `\\
   /::=========.:.-::"\\ \\ \\--\\   \\
    \\`""""""""""""""""`/  \\ \\__)   \\
    `""""""""""""""""`    '========'
'''
        showLessonTable.add_row(art)
        console.print(showLessonTable)

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
