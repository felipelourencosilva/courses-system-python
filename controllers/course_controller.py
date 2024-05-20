from views.course_view import *
from entities.course import *
from controllers.module_controller import *
import random


class CourseController:
    def __init__(self, system_controller):
        self.__courses = dict()
        self.__course_view = CourseView()
        self.__system_controller = system_controller
        self.__module_controller = ModuleController(self, system_controller)

    def get_producer(self, cpf: int):
        return self.__system_controller.producer_controller.get_producer_by_cpf(cpf)

    def get_course(self, id):
        if id in self.__courses:
            return self.__courses[id]
        else:
            return None

    def get_courses(self):
        return self.__courses

    def add_course_module(self, id: int, module: Module):
        course = self.get_course(id)
        course.add_module(module)

    def remove_course_module(self, course_id: int, module: Module):
        course = self.get_course(course_id)
        course.remove_module(module)

    def generate_id(self):
        id = random.randint(1, 1000)
        while id in self.__courses:
            id = random.randint(1, 1000)
        return id

    def add_course(self):
        if len(self.__system_controller.producer_controller.get_producers()) == 0:
            self.__course_view.show_message("Não é possível adicionar um Curso sem um Produtor cadastrado no sistema.")
            return
        course_data = self.__course_view.get_edit_course_data()
        self.__system_controller.producer_controller.list_producer()
        while True:
            cpf = self.__course_view.read_cpf("CPF do Produtor: ")
            if self.get_producer(cpf) is None:
                self.__course_view.show_message("Este produtor não existe")
            else:
                course_data["cpf"] = cpf
                break

        id = self.generate_id()
        course = Course(course_data["name"], self.get_producer(course_data["cpf"]),
                        course_data["description"], course_data["price"], course_data["commission_percentage"], id)
        self.__courses[id] = course
        self.__course_view.show_success_message("Curso adicionado com sucesso")

    def edit_course(self):
        if len(self.__courses) == 0:
            self.__course_view.show_message("Não há cursos cadastrados")
            return
        self.list_courses()
        id = self.__course_view.read_id()
        if id not in self.__courses:
            self.__course_view.show_message("Este curso não existe")
            return

        if id is not None and id in self.__courses:
            course_data = self.__course_view.get_edit_course_data()
            course = self.__courses[id]
            course.name = course_data["name"]
            course.description = course_data["description"]
            course.price = course_data["price"]
            course.commission_percentage = course_data["commission_percentage"]
            self.__course_view.show_success_message("Curso editado com sucesso")
        else:
            self.__course_view.show_message("Este curso não existe")

    def list_courses(self):
        if len(self.__courses) == 0:
            self.__course_view.show_message("Não há cursos cadastrados")
            return
        for key, course in self.__courses.items():
            self.__course_view.show_course({"name": course.name, "description": course.description, "price": course.price,
                                            "id": key, "producer": f"{course.producer.name} {course.producer.surname}"})

    def remove_course(self):
        if len(self.__courses) == 0:
            self.__course_view.show_message("Não há cursos cadastrados")
            return
        self.list_courses()
        id = self.__course_view.read_id()

        if id is not None and id in self.__courses:
            self.__courses.pop(id)
            self.__course_view.show_success_message("Curso removido com sucesso")
        else:
            self.__course_view.show_message("Este curso não existe")

    def buy_course(self):
        if len(self.__system_controller.user_controller.get_users()) == 0:
            self.__course_view.show_message("Não é possível comprar um Curso sem um Usuário cadastrado no sistema")
            return
        if len(self.__courses) == 0:
            self.__course_view.show_message("Não há cursos cadastrados")
            return
        self.list_courses()
        id = self.__course_view.read_id()
        if id not in self.__courses:
            self.__course_view.show_message("Este curso não existe")
            return

        if len(self.__system_controller.user_controller.get_proper_users()):
            self.__system_controller.user_controller.list_users()
        if len(self.__system_controller.producer_controller.get_producers()):
            self.__system_controller.producer_controller.list_producer()
        if len(self.__system_controller.affiliate_controller.get_affiliates()):
            self.__system_controller.affiliate_controller.list_affiliates()

        while True:
            cpf = self.__course_view.read_cpf("CPF do Usuário: ")
            if self.__system_controller.user_controller.get_user_by_cpf(cpf) is None:
                self.__course_view.show_message("Este usuário não existe")
            else:
                break

        course = self.__courses[id]
        if self.__system_controller.user_controller.user_has_course(cpf, course):
            self.__course_view.show_message("Você já possui esse curso")
            return
        if not (self.__system_controller.user_controller.user_has_enough_balance(cpf, course)):
            self.__course_view.show_message("Você não possui saldo suficiente")
            return

        if len(self.__system_controller.affiliate_controller.get_affiliates()) != 0:
            self.__system_controller.affiliate_controller.list_affiliates()
        affiliate = None
        while True:
            affiliate_cpf = self.__course_view.read_int("CPF do Afiliado (coloque 0 se não houver Afiliado): ", "CPF deve ser inteiro positivo ou 0.")
            if affiliate_cpf == 0:
                break
            if self.__system_controller.affiliate_controller.get_affiliate_by_cpf(affiliate_cpf) is None:
                self.__course_view.show_message("Este afiliado não existe")
            else:
                affiliate = self.__system_controller.affiliate_controller.get_affiliate_by_cpf(affiliate_cpf)
                break

        self.__system_controller.user_controller.user_add_course(cpf, course)
        self.__system_controller.producer_controller.pay_producer(course, affiliate is not None)
        self.__system_controller.affiliate_controller.pay_affiliate(course, affiliate)
        user = self.__system_controller.user_controller.get_user_by_cpf(cpf)
        self.__system_controller.sale_controller.add_sale(user, course, affiliate)
        self.__course_view.show_success_message("Curso adquirido com sucesso")

    def module_controller(self):
        self.__module_controller.show_view()

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_course,
            2: self.edit_course,
            3: self.list_courses,
            4: self.buy_course,
            5: self.module_controller,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__course_view.view_options()
            options[chosen_option]()
