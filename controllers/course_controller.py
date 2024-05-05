from views.course_view import *
from entities.course import *
import random


class CourseController:
    def __init__(self, system_controller):
        self.__courses = dict()
        self.__course_view = CourseView()
        self.__system_controller = system_controller

    def get_producer(self, cpf: int):
        return self.__system_controller.producer_controller.get_producer_by_cpf(cpf)

    def generate_id(self):
        id = random.randint(1, 1000)
        while id in self.__courses:
            id = random.randint(1, 1000)
        return id

    def add_course(self):
        course_data = self.__course_view.get_add_course_data()
        id = self.generate_id()
        course = Course(course_data["name"], self.get_producer(course_data["cpf"]),
                        course_data["description"], course_data["price"], course_data["commission_percentage"], id)
        self.__courses[id] = course

    def edit_course(self):
        self.list_courses()
        id = self.__course_view.read_id()

        if id is not None and id in self.__courses:
            course_data = self.__course_view.get_edit_course_data()
            course = self.__courses[id]
            course.name = course_data["name"]
            course.description = course_data["description"]
            course.price = course_data["price"]
            course.commission_percentage = course_data["commission_percentage"]
        else:
            self.__course_view.show_message("Curso não encontrado ou id incorreto")

    def list_courses(self):
        if len(self.__courses) == 0:
            self.__course_view.show_message("Não há cursos cadastrados")
        else:
            for key, course in self.__courses.items():
                self.__course_view.show_course({"name": course.name, "description": course.description, "price": course.price,
                                                "id": key})

    def remove_course(self):
        self.list_courses()
        id = self.__course_view.read_id()

        if id is not None and id in self.__courses:
            self.__courses.pop(id)
        else:
            self.__course_view.show_message("Curso não encontrado ou id incorreto")

    def buy_course(self):
        self.list_courses()
        id = self.__course_view.read_id()
        cpf = self.__course_view.read_cpf()

        if id is not None and id in self.__courses:
            course = self.__courses[id]
            if self.__system_controller.user_controller.user_has_course(cpf, course):
                self.__course_view.show_message("Você já possui esse curso")
            if not (self.__system_controller.user_controller.user_has_enough_balance(cpf, course)):
                self.__course_view.show_message("Você não possui saldo suficiente")
            else:
                self.__system_controller.user_controller.user_add_course(cpf, course)

        else:
            self.__course_view.show_message("Curso não encontrado ou id incorreto")

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_course,
            2: self.edit_course,
            3: self.list_courses,
            4: self.buy_course,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__course_view.view_options()
            options[chosen_option]()
