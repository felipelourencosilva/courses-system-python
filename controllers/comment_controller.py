from views.comment_view import *
from entities.comment import *
import random


class CommentController:
    __instance = None

    def __init__(self, lesson_controller, system_controller):
        self.__comments = dict()
        self.__lesson_controller = lesson_controller
        self.__system_controller = system_controller
        self.__comment_view = CommentView()

    '''
    def __new__(cls):
        if CommentController.__instance is None:
            CommentController.__instance = object.__new__(cls)
        return CommentController.__instance
    '''
    def generate_id(self):
        id = random.randint(1, 1000)
        while id in self.__comments:
            id = random.randint(1, 1000)
        return id

    def add_comment(self):
        if len(self.__lesson_controller.get_lessons()) == 0:
            self.__comment_view.show_message("Não é possível adicionar um Comentário sem uma Aula no sistema")
            return

        course_id = self.__lesson_controller.list_lessons()

        if course_id == -1:
            return

        if len(self.__system_controller.user_controller.get_proper_users()):
            self.__system_controller.user_controller.list_users()
        if len(self.__system_controller.producer_controller.get_producers()):
            self.__system_controller.producer_controller.list_producer()
        if len(self.__system_controller.affiliate_controller.get_affiliates()):
            self.__system_controller.affiliate_controller.list_affiliates()

        comment_data = self.__comment_view.get_comment_data()
        user_cpf = int(comment_data["user_cpf"])
        lesson_id = int(comment_data["lesson_id"])
        user = self.__system_controller.user_controller.get_user_by_cpf(user_cpf)

        if lesson_id in self.__lesson_controller.get_lessons():
            comment_id = self.generate_id()
            comment = Comment(user, comment_data["comment"], comment_id)
            self.__lesson_controller.add_lesson_comment(lesson_id, comment)
            self.__comments[comment_id] = comment
            self.__comment_view.show_success_message("Comentário adicionado com sucesso")
        else:
            self.__comment_view.show_message("Esta aula não existe")

    def remove_comment(self):
        if len(self.__comments) == 0:
            self.__comment_view.show_message("Não há comentários cadastrados")
            return

        lesson_id = self.list_comments()

        if lesson_id == -1:
            return

        comment_id = self.__comment_view.read_comment_id()
        if comment_id is not None and comment_id in self.__comments:
            comment = self.__comments[comment_id]
            self.__comments.pop(comment_id)
            self.__lesson_controller.remove_lesson_comment(lesson_id, comment)
            self.__comment_view.show_success_message("Comentário removido com sucesso")
        else:
            self.__comment_view.show_message("Este comentário não existe")

    def edit_comment(self):
        if len(self.__comments) == 0:
            self.__comment_view.show_message("Não há comentários cadastrados")
            return

        self.list_comments()
        comment_data = self.__comment_view.get_edit_comment_data()
        comment_id = int(comment_data["comment_id"])

        if comment_id is not None and comment_id in self.__comments:

            comment = self.__comments[comment_id]
            comment.comment = comment_data["comment"]
            self.__comment_view.show_success_message("Comentário editado com sucesso")
        else:
            self.__comment_view.show_message("Este comentário não existe")

    def list_comments(self):
        if len(self.__comments) == 0:
            self.__comment_view.show_message("Não há comentários cadastrados")
            return -1

        course_id = self.__lesson_controller.list_lessons()
        if course_id == -1:
            return -1
        lesson_id = self.__comment_view.read_lesson_id()
        if lesson_id == -1:
            return -1
        lesson = self.__lesson_controller.get_lesson(lesson_id)

        if lesson is not None:
            if len(lesson.comments) == 0:
                self.__comment_view.show_message("Não há comentários cadastrados nessa aula")
            else:
                comments_info = []
                for comment in lesson.comments:
                    comments_info.append([comment, comment.id])
                self.__comment_view.show_comment(comments_info)
            return lesson_id
        else:
            self.__comment_view.show_message("Aula não encontrada")
            return -1

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
