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

        course_id = self.__system_controller.course_controller.list_courses()
        if course_id is None:
            return

        module_id = self.__system_controller.course_controller.module_controller.list_modules(course_id)
        if module_id is None:
            return

        lesson_id = self.__lesson_controller.list_lessons(course_id, module_id)
        if lesson_id is None:
            return

        user_cpf = self.__system_controller.user_controller.list_users()
        if user_cpf is None:
            return

        comment_data = self.__comment_view.get_comment_data()
        if comment_data is None:
            return

        user = self.__system_controller.user_controller.get_user_by_cpf(user_cpf)
        comment_id = self.generate_id()
        comment = Comment(user, comment_data["comment"], comment_id)
        self.__lesson_controller.add_lesson_comment(lesson_id, comment)
        self.__comments[comment_id] = comment
        self.__comment_view.show_success_message("Comentário adicionado com sucesso")

    def remove_comment(self):
        if len(self.__comments) == 0:
            self.__comment_view.show_message("Não há comentários cadastrados")
            return

        course_id = self.__module_controller.course_controller.list_courses()
        if course_id is None:
            return

        module_id = self.__module_controller.list_modules(course_id)
        if module_id is None:
            return

        lesson_id = self.__lesson_controller.list_lessons(course_id, module_id)
        if lesson_id is None:
            return

        comment_id = self.list_comments()
        if comment_id is None:
            return

        comment = self.__comments[comment_id]
        self.__comments.pop(comment_id)
        self.__lesson_controller.remove_lesson_comment(lesson_id, comment)
        self.__comment_view.show_success_message("Comentário removido com sucesso")

    def edit_comment(self):
        if len(self.__comments) == 0:
            self.__comment_view.show_message("Não há comentários cadastrados")
            return

        course_id = self.__system_controller.course_controller.list_courses()
        if course_id is None:
            return

        module_id = self.__system_controller.module_controller.list_modules(course_id)
        if module_id is None:
            return

        lesson_id = self.__lesson_controller.list_lessons(course_id, module_id)
        if lesson_id is None:
            return

        comment_id = self.list_comments(course_id, module_id, lesson_id)
        if comment_id is None:
            return

        comment_data = self.__comment_view.get_edit_comment_data()
        if comment_data is None:
            return

        comment = self.__comments[comment_id]
        comment.comment = comment_data["comment"]
        self.__comment_view.show_success_message("Comentário editado com sucesso")

    def list_comments(self, lesson_id=None):
        if len(self.__comments) == 0:
            self.__comment_view.show_message("Não há comentários cadastrados")
            return

        if lesson_id is None:
            lesson_id = self.__lesson_controller.list_lessons()
            if lesson_id is None:
                return

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
