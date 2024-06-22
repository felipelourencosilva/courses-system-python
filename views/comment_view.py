from views.abstract_view import AbstractView
import PySimpleGUI as sg


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
        return super().view_options("COMENTÁRIOS", options)

    def get_comment_data(self):
        layout = [
            [sg.Text(f'Escreva seu comentário:', font=("Helvica", 25))],
            [sg.Text('Comentário:', size=(15, 1)), sg.InputText('', key='comment')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar comentário').Layout(layout)

        button, values = self.open(edit_module_window)
        comment = values['comment']
        edit_module_window.Close()

        return {"comment": comment}

    def show_comment(self, comments, lesson_name):
        layout = [
            [sg.Text(f'Comentários da aula: {lesson_name}: ', font=("Helvica", 25))],
        ]

        for comment in comments:
            layout.extend(
                [[sg.Text(f'{comment["comment"]}', size=(60, 1))],
                 [sg.Text(f'Id: {comment["id"]}', size=(60, 1))],
                 [sg.Text('', size=(60, 1))]]
            )

        layout.append([sg.Button('Confirmar')])
        show_users_window = sg.Window('Aulas').Layout(layout)

        button, values = self.open(show_users_window)
        show_users_window.Close()

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
