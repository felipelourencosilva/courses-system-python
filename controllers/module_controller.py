from views.module_view import *
from controllers.lesson_controller import *


class ModuleController:
    def __init__(self, course_controller):
        self.__modules = []
        self.__course_controller = course_controller
        self.__module_view = ModuleView()
        self.__lesson_controller = LessonController(self)

    def lesson_controller(self):
        self.__lesson_controller.show_view()

    def previous_view(self):
        self.__course_controller.show_view()

    def show_view(self):
        options = {
            5: self.lesson_controller,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__module_view.view_options()
            options[chosen_option]()
