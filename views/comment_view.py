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
        edit_module_window.Close()

        if button in (None, 'Cancelar'):
            return
        return values

    def get_edit_comment_data(self):
        layout = [
            [sg.Text(f'Escreva seu comentário:', font=("Helvica", 25))],
            [sg.Text('Comentário:', size=(15, 1)), sg.InputText('', key='comment')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        edit_module_window = sg.Window('Criar comentário').Layout(layout)
        button, values = self.open(edit_module_window)
        edit_module_window.Close()

        if button in (None, 'Cancelar'):
            return
        return values

    def show_comment(self, comment_data):
        headings = ["Comentário", "Id"]
        layout = [[sg.Table(values=comment_data, headings=headings, max_col_width=25, background_color='#0F0E10',
                            auto_size_columns=True,
                            justification='right',
                            num_rows=6,
                            alternating_row_color='#1C2C30',
                            key='comment',
                            select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
                  [sg.Button('Confirmar'), sg.Button('Voltar')]]

        show_lessons_window = sg.Window('Comentários').Layout(layout)
        button, values = self.open(show_lessons_window)
        show_lessons_window.Close()

        if button in (None, 'Voltar'):
            return None

        selected_rows = values["comment"]
        if len(selected_rows) == 0:
            return None  # no selected Comment
        comment_row = values["comment"][0]
        comment_id = comment_data[comment_row][1]  # because 1st position is the id
        return int(comment_id)

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
