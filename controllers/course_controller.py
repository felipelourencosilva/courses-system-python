from exceptions.empty_input_exception import EmptyInputException
from exceptions.missing_entity_exception import MissingEntityException
from exceptions.missing_parent_exception import MissingParentException
from exceptions.negative_value_exception import NegativeValueException
from exceptions.wrong_input_exception import WrongInputException
from exceptions.not_enough_balance_exception import NotEnoughBalanceException
from exceptions.repeated_course_exception import RepeatedCourseException
from views.course_view import *
from entities.course import *
from controllers.module_controller import *
import random


class CourseController:
    __instance = None

    def __init__(self, system_controller):
        self.__courses = dict()
        self.__course_view = CourseView()
        self.__system_controller = system_controller
        self.__module_controller = system_controller.get_state_of_controller("module_controller")
        if self.__module_controller is None:
            self.__module_controller = ModuleController(self, system_controller)

    def __new__(cls, *args, **kwargs):
        if CourseController.__instance is None:
            CourseController.__instance = super(CourseController, cls).__new__(cls)
        return CourseController.__instance

    @property
    def module_controller(self):
        return self.__module_controller

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
        try:
            if len(self.__system_controller.producer_controller.get_producers()) == 0:
                raise MissingParentException("Não é possível adicionar um Curso sem um Produtor cadastrado no sistema.")

            producer_cpf = self.__system_controller.producer_controller.list_producer()
            if producer_cpf is None:
                return

            course_data = self.__course_view.get_add_course_data()
            if course_data is None:
                return

            if (course_data["name"] == "" or course_data["description"] == "" or course_data["price"] == "" or
                    course_data["commission_percentage"] == ""):
                raise EmptyInputException()

            try:
                float(course_data["price"])
                float(course_data["commission_percentage"])
            except ValueError:
                raise WrongInputException('Digite os valores corretamente para o preço e porcentagem de comissão.')

            if float(course_data["price"]) < 0 or int(course_data["commission_percentage"]) < 0:
                raise WrongInputException('Valores devem ser maiores do que 0.')

            if int(course_data["commission_percentage"]) > 100:
                raise WrongInputException('A porcentagem deve ser menor ou igual a 100.')

            course_data["price"] = float(course_data["price"])
            course_data["commission_percentage"] = int(course_data["commission_percentage"])

            id = self.generate_id()
            producer = self.get_producer(producer_cpf)
            course = Course(
                course_data["name"],
                producer,
                course_data["description"],
                course_data["price"],
                course_data["commission_percentage"],
                id
            )
            self.__courses[id] = course
            self.__course_view.show_success_message("Curso adicionado com sucesso")
        except (MissingParentException, EmptyInputException, WrongInputException) as e:
            self.__course_view.show_message(e)

    def edit_course(self):
        try:
            if len(self.__courses) == 0:
                raise MissingEntityException("Não há cursos cadastrados.")

            id = self.list_courses()
            if id is None:
                return
            if id not in self.__courses:
                raise MissingEntityException("Este curso não existe.")

            course = self.__courses[id]
            course_info = {"name": course.name, "description": course.description,
                           "price": course.price, "commission_percentage": course.commission_percentage}

            course_data = self.__course_view.get_edit_course_data(course_info)
            if course_data is None:
                return

            if (course_data["name"] == "" or course_data["description"] == "" or course_data["price"] == "" or
                    course_data["commission_percentage"] == ""):
                raise EmptyInputException()

            try:
                float(course_data["price"])
                float(course_data["commission_percentage"])
            except ValueError:
                raise WrongInputException('Digite os valores corretamente para o preço e porcentagem de comissão.')

            if float(course_data["price"]) < 0 or int(course_data["commission_percentage"]) < 0:
                raise WrongInputException('Valores devem ser maiores do que 0.')

            if int(course_data["commission_percentage"]) > 100:
                raise WrongInputException('A porcentagem deve ser menor ou igual a 100.')

            course_data["price"] = float(course_data["price"])
            course_data["commission_percentage"] = int(course_data["commission_percentage"])

            course.name = course_data["name"]
            course.description = course_data["description"]
            course.price = course_data["price"]
            course.commission_percentage = course_data["commission_percentage"]
            self.__course_view.show_success_message("Curso editado com sucesso")
        except (MissingEntityException, EmptyInputException, WrongInputException) as e:
            self.__course_view.show_message(e)

    def list_courses(self):
        try:
            if len(self.__courses) == 0:
                raise MissingEntityException("Não há cursos cadastrados.")

            courses_data = []
            for key, course in self.__courses.items():
                courses_data.append([
                    course.name,
                    course.description,
                    course.price,
                    key,
                    f"{course.producer.name} {course.producer.surname}"
                ])
            return self.__course_view.show_courses(courses_data)
        except MissingEntityException as e:
            self.__course_view.show_message(e)

    def buy_course(self):
        try:
            if len(self.__system_controller.user_controller.get_users()) == 0:
                raise MissingParentException("Não é possível comprar um Curso sem um Usuário cadastrado no sistema")
            if len(self.__courses) == 0:
                raise MissingEntityException("Não há cursos cadastrados")

            course_id = self.list_courses()
            if course_id is None:
                return
            cpf = self.__system_controller.user_controller.list_users()
            if cpf is None:
                return
            course = self.__courses[course_id]

            if self.__system_controller.user_controller.user_has_course(cpf, course):
                raise RepeatedCourseException()
            if not self.__system_controller.user_controller.user_has_enough_balance(cpf, course):
                raise NotEnoughBalanceException()

            affiliate_cpf = self.__system_controller.affiliate_controller.list_affiliates(True)
            if affiliate_cpf is None:
                return
            affiliate = None
            if affiliate_cpf != -1:  # if the user did not select the "no affiliate" button
                affiliate = self.__system_controller.affiliate_controller.get_affiliate_by_cpf(affiliate_cpf)

            self.__system_controller.user_controller.user_add_course(cpf, course)
            self.__system_controller.producer_controller.pay_producer(course, affiliate is not None)
            self.__system_controller.affiliate_controller.pay_affiliate(course, affiliate)
            user = self.__system_controller.user_controller.get_user_by_cpf(cpf)
            self.__system_controller.sale_controller.add_sale(user, course, affiliate)
            self.__course_view.show_success_message("Curso adquirido com sucesso")
        except (MissingParentException, WrongInputException,
                RepeatedCourseException, NotEnoughBalanceException, MissingEntityException) as e:
            self.__course_view.show_message(e)

    def to_module_view(self):
        self.__module_controller.show_view()

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            1: self.add_course,
            2: self.edit_course,
            3: self.list_courses,
            4: self.buy_course,
            5: self.to_module_view,
            0: self.previous_view
        }

        while True:
            chosen_option = self.__course_view.view_options()
            options[chosen_option]()
