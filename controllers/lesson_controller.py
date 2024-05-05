from views.lesson_view import *


class LessonController:
    def __init__(self, module_controller):
        self.__lessons = []
        self.__module_controller = module_controller
        self.__lesson_view = LessonView()

    def previous_view(self):
        self.__module_controller.show_view()

    def show_view(self):
        options = {
            0: self.previous_view
        }

        while True:
            chosen_option = self.__lesson_view.view_options()
            options[chosen_option]()
