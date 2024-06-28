from views.module_view import *
from controllers.lesson_controller import *
from entities.module import *
import random


class ModuleController:
    __instance = None

    def __init__(self, course_controller, system_controller):
        self.__modules = dict()
        self.__course_controller = course_controller
        self.__module_view = ModuleView()
        self.__lesson_controller = system_controller.get_state_of_controller("lesson_controller")
        if self.__lesson_controller is None:
            self.__lesson_controller = LessonController(self, system_controller)

    '''
    def __new__(cls):
        if ModuleController.__instance is None:
            ModuleController.__instance = object.__new__(cls)
        return ModuleController.__instance
    '''
    @property
    def course_controller(self):
        return self.__course_controller

    @property
    def lesson_controller(self):
        return self.__lesson_controller

    def generate_id(self):
        id = random.randint(1, 1000)
        while id in self.__modules:
            id = random.randint(1, 1000)
        return id

    def get_modules(self):
        return self.__modules

    def get_module(self, id):
        if id in self.__modules:
            return self.__modules[id]
        else:
            return None

    def add_module_lesson(self, id: int, lesson: Lesson):
        if id is not None and id in self.__modules and isinstance(lesson, Lesson):
            module = self.get_module(id)
            module.add_lesson(lesson)
        else:
            self.__module_view.show_message("Este curso não existe")

    def remove_module_lesson(self, id: int, lesson: Lesson):
        module = self.get_module(id)
        module.remove_lesson(lesson)

    def add_module(self):
        if len(self.__course_controller.get_courses()) == 0:
            self.__module_view.show_message("Não é possível adicionar um Módulo sem um Curso no sistema")
            return

        course_id = self.__course_controller.list_courses()
        if course_id is None:
            return

        module_data = self.__module_view.get_add_module_data()
        if module_data is None:
            return

        module_id = self.generate_id()
        module = Module(module_data["title"], module_data["description"], module_id)
        self.__course_controller.add_course_module(course_id, module)
        self.__modules[module_id] = module
        self.__module_view.show_success_message("Módulo adicionado com sucesso")

    def remove_module(self):
        if len(self.__modules) == 0:
            self.__module_view.show_message("Não há módulos cadastrados")
            return

        course_id = self.course_controller.list_courses()
        if course_id is None:
            return
        module_id = self.list_modules(course_id)
        if module_id is None:
            return

        if self.__modules[module_id] not in self.__course_controller.get_course(course_id).modules:
            self.__module_view.show_message("Este módulo não pertence a este curso")
            return
        module = self.__modules[module_id]
        self.__modules.pop(module_id)
        self.__course_controller.remove_course_module(course_id, module)
        self.__module_view.show_success_message("Módulo removido com sucesso")

    def edit_module(self):
        if len(self.__modules) == 0:
            self.__module_view.show_message("Não há módulos cadastrados")
            return

        course_id = self.__course_controller.list_courses()
        if course_id is None:
            return
        module_id = self.list_modules(course_id)
        if module_id is None:
            return
        module_data = self.__module_view.get_edit_module_data()
        if module_data is None:
            return

        if self.__modules[module_id] not in self.__course_controller.get_course(course_id).modules:
            self.__module_view.show_message("Este módulo não pertence a este curso")
            return

        module = self.__modules[module_id]
        module.title = module_data["title"]
        module.description = module_data["description"]
        self.__module_view.show_success_message("Módulo editado com sucesso")

    def list_modules(self, course_id=None):
        if len(self.__modules) == 0:
            self.__module_view.show_message("Não há módulos cadastrados")
            return

        if course_id is None:
            course_id = self.course_controller.list_courses()
            if course_id is None:
                return

        course = self.__course_controller.get_course(course_id)

        if len(course.modules) == 0:
            self.__module_view.show_message("Não há módulos cadastrados nesse curso")
            return

        modules_info = []
        for module in course.modules:
            modules_info.append([module.title, module.description,
                                 module.id])
        module_id = self.__module_view.show_modules(modules_info)
        return module_id

    def to_lesson_view(self):
        self.__lesson_controller.show_view()

    def previous_view(self):
        self.__course_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_module,
            2: self.remove_module,
            3: self.edit_module,
            4: self.list_modules,
            5: self.to_lesson_view,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__module_view.view_options()
            options[chosen_option]()
