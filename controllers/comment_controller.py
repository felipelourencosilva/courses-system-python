from views.comment_view import *
from entities.comment import *
import random


class CommentController:
    def __init__(self, lesson_controller, system_controller):
        self.__comments = dict()
        self.__lesson_controller = lesson_controller
        self.__system_controller = system_controller
        self.__comment_view = CommentView()

    def generate_id(self):
        id = random.randint(1, 1000)
        while id in self.__comments:
            id = random.randint(1, 1000)
        return id

    def add_comment(self):
        if len(self.__lesson_controller.get_lessons()) == 0:
            self.__comment_view.show_message("Não é possível adicionar um Comentário sem uma Aula no sistema")
            return
        self.__lesson_controller.list_lessons()
        lesson_id = self.__comment_view.read_lesson_id()
        self.__system_controller.user_controller.list_users()
        user_cpf = self.__comment_view.read_cpf("CPF do autor: ")

        if (lesson_id is not None and user_cpf is not None and lesson_id in self.__lesson_controller.get_lessons() and
            user_cpf in self.__system_controller.user_controller.get_users()):
            comment_data = self.__comment_view.get_comment_data()
            comment_id = self.generate_id()

            user = self.__system_controller.user_controller.get_user_by_cpf(user_cpf)
            if user is not None:
                comment = Comment(user, comment_data["comment"], comment_id)
                self.__lesson_controller.add_lesson_comment(lesson_id, comment)
                self.__comments[comment_id] = comment
            else:
                self.__comment_view.show_message("Este comentário não existe")
        else:
            self.__comment_view.show_message("Este comentário não existe")

    def remove_comment(self):
        if len(self.__comments) == 0:
            self.__comment_view.show_message("Não há comentários cadastrados")
            return
        comment_id = self.__comment_view.read_comment_id()
        lesson_id = self.__comment_view.read_lesson_id()
        if comment_id is not None and comment_id in self.__comments:
            comment = self.__comments[comment_id]
            self.__comments.pop(comment)
            self.__lesson_controller.remove_lesson_comment(lesson_id, comment)
        else:
            self.__comment_view.show_message("Este comentário não existe")

    def edit_comment(self):
        if len(self.__comments) == 0:
            self.__comment_view.show_message("Não há comentários cadastrados")
            return
        self.list_comments()
        comment_id = self.__comment_view.read_comment_id()

        if comment_id is not None and comment_id in self.__comments:
            comment_data = self.__comment_view.get_comment_data()
            comment = self.__comments[comment_id]
            comment.comment = comment_data["comment"]
        else:
            self.__comment_view.show_message("Este comentário não existe")

    def list_comments(self):
        if len(self.__comments) == 0:
            self.__comment_view.show_message("Não há comentarios cadastrados")
            return
        lesson_id = self.__comment_view.read_lesson_id()
        lesson = self.__lesson_controller.get_lesson(lesson_id)

        if lesson is not None:
            if len(lesson.comments) == 0:
                self.__comment_view.show_message("Não há comentários cadastrados nessa aula")
            else:
                for comment in lesson.comments:
                    self.__comment_view.show_comment({"comment": comment})
        else:
            self.__comment_view.show_message("Aula não encontrada")

    def previous_view(self):
        self.__lesson_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_comment,
            2: self.remove_comment,
            3: self.edit_comment,
            4: self.list_comments,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__comment_view.view_options()
            options[chosen_option]()
