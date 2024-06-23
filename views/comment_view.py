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
            [sg.Text('CPF do autor:', size=(15, 1)), sg.InputText('', key='user_cpf')],
            [sg.Text('Id da aula:', size=(15, 1)), sg.InputText('', key='lesson_id')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar comentário').Layout(layout)

        button, values = self.open(edit_module_window)
        comment = values['comment']
        user_cpf = values['user_cpf']
        lesson_id = values['lesson_id']
        edit_module_window.Close()

        return {"comment": comment, "user_cpf": user_cpf, "lesson_id": lesson_id}

    def get_edit_comment_data(self):
        layout = [
            [sg.Text(f'Escreva seu comentário:', font=("Helvica", 25))],
            [sg.Text('Comentário:', size=(15, 1)), sg.InputText('', key='comment')],
            [sg.Text('Id do comentário:', size=(15, 1)), sg.InputText('', key='comment_id')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar comentário').Layout(layout)

        button, values = self.open(edit_module_window)
        comment = values['comment']
        comment_id = values['comment_id']
        edit_module_window.Close()

        return {"comment": comment, "comment_id": comment_id}

    def show_comment(self, comments):
        headings = ["Comentário", "id"]
        layout = [[sg.Table(values=comments, headings=headings, max_col_width=25, background_color='lightblue',
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='lightyellow',
                            key='-TABLE-')],
                  [sg.Button('Voltar')]]

        show_users_window = sg.Window('Cursos').Layout(layout)
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
