from views.lesson_view import *
from entities.lesson import *
from controllers.comment_controller import *
import random


class LessonController:
    __instance = None

    def __init__(self, module_controller, system_controller):
        self.__lessons = dict()
        self.__module_controller = module_controller
        self.__lesson_view = LessonView()
        self.__comment_controller = system_controller.get_state_of_controller("comment_controller")
        if self.__comment_controller is None:
            self.__comment_controller = CommentController(self, system_controller)

    '''
    def __new__(cls):
        if LessonController.__instance is None:
            LessonController.__instance = object.__new__(cls)
        return LessonController.__instance
    '''
    @property
    def comment_controller(self):
        return self.__comment_controller

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
            self.__lesson_view.show_message("Esta aula não existe")

    def remove_lesson_comment(self, id: int, comment: Comment):
        if id is not None and id in self.__lessons and isinstance(comment, Comment):
            lesson = self.get_lesson(id)
            lesson.remove_comment(comment)
        else:
            self.__lesson_view.show_message("Esta aula não existe")

    def add_lesson(self):
        if len(self.__module_controller.get_modules()) == 0:
            self.__lesson_view.show_message("Não é possível adicionar uma Aula sem um Módulo no sistema")
            return

        course_id = self.__module_controller.course_controller.list_courses()
        if course_id is None:
            return

        module_id = self.__module_controller.list_modules(course_id)
        if module_id is None:
            return

        lesson_data = self.__lesson_view.get_lesson_data()
        if lesson_data is None:
            return

        lesson_id = self.generate_id()
        lesson = Lesson(lesson_data["title"], lesson_data["description"], Video(lesson_data["video_url"]), lesson_id)
        self.__module_controller.add_module_lesson(module_id, lesson)
        self.__lessons[lesson_id] = lesson
        self.__lesson_view.show_success_message("Aula adicionada com sucesso")


    def remove_lesson(self):
        if len(self.__lessons) == 0:
            self.__lesson_view.show_message("Não há aulas cadastradas")
            return

        course_id = self.__module_controller.course_controller.list_courses()
        if course_id is None:
            return

        module_id = self.__module_controller.list_modules(course_id)
        if module_id is None:
            return

        lesson_id = self.list_lessons()
        if lesson_id is None:
            return

        if self.__lessons[lesson_id] not in self.__module_controller.get_module(module_id).lessons:
            self.__lesson_view.show_message("Esta aula não pertence a este módulo")
            return
        lesson = self.__lessons.pop(lesson_id)
        self.__module_controller.remove_module_lesson(module_id, lesson)
        self.__lesson_view.show_success_message("Aula removida com sucesso")

    def edit_lesson(self):
        if len(self.__lessons) == 0:
            self.__lesson_view.show_message("Não há aulas cadastradas")
            return

        course_id = self.__module_controller.course_controller.list_courses()
        if course_id is None:
            return

        module_id = self.__module_controller.list_modules(course_id)
        if module_id is None:
            return

        lesson_id = self.list_lessons(course_id, lesson_id)
        if lesson_id is None:
            return

        lesson_data = self.__lesson_view.get_edit_lesson_data()
        lesson = self.__lessons[lesson_id]
        lesson.title = lesson_data["title"]
        lesson.description = lesson_data["description"]
        lesson.video = Video(lesson_data["video_url"])
        self.__lesson_view.show_success_message("Aula editada com sucesso")

    def list_lessons(self, course_id=None, module_id=None):
        if len(self.__lessons) == 0:
            self.__lesson_view.show_message("Não há aulas cadastradas")
            return

        if course_id is None:
            course_id = self.__module_controller.course_controller.list_courses()
            if course_id is None:
                return

        if module_id is None:
            module_id = self.__module_controller.list_modules(course_id)
            if module_id is None:
                return

        module = self.__module_controller.get_module(module_id)
        if len(module.lessons) == 0:
            self.__lesson_view.show_message("Não há aulas cadastradas nesse módulo")
            return

        lesson_data = []
        for lesson in module.lessons:
            lesson_data.append([lesson.title, lesson.description,
                                 lesson.id, lesson.video])
        lesson_id = self.__lesson_view.show_lessons(lesson_data)
        return lesson_id

    def previous_view(self):
        self.__module_controller.show_view()

    def to_comment_view(self):
        self.__comment_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_lesson,
            2: self.remove_lesson,
            3: self.edit_lesson,
            4: self.list_lessons,
            5: self.to_comment_view,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__lesson_view.view_options()
            options[chosen_option]()
