from views.lesson_view import *
from entities.lesson import *
from entities.comment import *
from controllers.comment_controller import *
import random


class LessonController:
    def __init__(self, module_controller, system_controller):
        self.__lessons = dict()
        self.__module_controller = module_controller
        self.__lesson_view = LessonView()
        self.__comment_controller = CommentController(self, system_controller)

    def generate_id(self):
        id = random.randint(1, 1000)
        while id in self.__lessons:
            id = random.randint(1, 1000)
        return id

    def get_lessons(self):
        return self.__lessons

    def get_lesson(self, id: int):
        if id in self.__lessons:
            return self.__lessons[id]
        else:
            return None

    def add_lesson_comment(self, id: int, comment: Comment):
        if id is not None and id in self.__lessons and isinstance(comment, Comment):
            lesson = self.get_lesson(id)
            lesson.add_comment(comment)
        else:
            self.__lesson_view.show_message("Aula não existe ou id incorreto")

    def remove_lesson_comment(self, id: int, comment: Comment):
        if id is not None and id in self.__lessons and isinstance(comment, Comment):
            lesson = self.get_lesson(id)
            lesson.remove_comment(comment)
        else:
            self.__lesson_view.show_message("Aula não existe ou id incorreto")

    def add_lesson(self):
        if len(self.__module_controller.get_modules()) == 0:
            self.__lesson_view.show_message("Não é possível adicionar uma Aula sem um Módulo no sistema.")
            return
        module_id = self.__lesson_view.read_module_id()
        if module_id is not None and module_id in self.__module_controller.get_modules():
            lesson_data = self.__lesson_view.get_lesson_data()
            lesson_id = self.generate_id()

            lesson = Lesson(lesson_data["title"], lesson_data["description"], Video(lesson_data["video_url"]), lesson_id)
            self.__module_controller.add_module_lesson(module_id, lesson)
            self.__lessons[lesson_id] = lesson
        else:
            self.__lesson_view.show_message("Módulo não encontrado ou id incorreto")

    def remove_lesson(self):
        if len(self.__lessons) == 0:
            self.__lesson_view.show_message("Não há aulas cadastradas")
            return
        lesson_id = self.__lesson_view.read_lesson_id()
        if lesson_id is not None and lesson_id in self.__lessons:
            lesson = self.__lessons[lesson_id]
            self.__lessons.pop(lesson)
            self.__module_controller.remove_module_lesson(lesson_id, lesson)
        else:
            self.__lesson_view.show_message("Aula não encontrada ou id incorreto")

    def edit_lesson(self):
        if len(self.__lessons) == 0:
            self.__lesson_view.show_message("Não há aulas cadastradas")
            return
        self.list_lessons()
        lesson_id = self.__lesson_view.read_lesson_id()

        if lesson_id is not None and lesson_id in self.__lessons:
            lesson_data = self.__lesson_view.get_lesson_data()
            lesson = self.__lessons[lesson_id]
            lesson.title = lesson_data["title"]
            lesson.description = lesson_data["description"]
            lesson.video = Video(lesson_data["video_url"])
        else:
            self.__lesson_view.show_message("Aula não encontrada ou id incorreto")

    def list_lessons(self):
        if len(self.__lessons) == 0:
            self.__lesson_view.show_message("Não há aulas cadastradas")
            return
        module_id = self.__lesson_view.read_module_id()
        module = self.__module_controller.get_module(module_id)

        if module is not None:
            if len(module.lessons) == 0:
                self.__lesson_view.show_message("Não há Aulas cadastrados nesse módulo")
            else:
                for lesson in module.lessons:
                    self.__lesson_view.show_lesson({"title": lesson.title, "description": lesson.description,
                                                    "id": lesson.id, "video_url": lesson.video})
        else:
            self.__lesson_view.show_message("Curso não encontrado")

    def previous_view(self):
        print("\033[H\033[J", end="")
        self.__module_controller.show_view()

    def comment_controller(self):
        self.__comment_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_lesson,
            2: self.remove_lesson,
            3: self.edit_lesson,
            4: self.list_lessons,
            5: self.comment_controller,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__lesson_view.view_options()
            options[chosen_option]()
