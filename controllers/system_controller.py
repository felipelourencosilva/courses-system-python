from views.system_view import *
from controllers.user_controller import *
from controllers.producer_controller import *
from controllers.affiliate_controller import *
from controllers.sale_controller import *
from controllers.course_controller import *
from entities.dao.systemDAO import SystemDAO


class SystemController:
    __instance = None

    def __init__(self):
        self.__system_dao = SystemDAO()
        self.__program_state = self.__system_dao.get("program_state")
        if self.__program_state is None:
            self.__program_state = dict()
        self.__init_controllers()
        self.__system_view = SystemView()

    def __new__(cls):
        if SystemController.__instance is None:
            SystemController.__instance = object.__new__(cls)
        return SystemController.__instance

    @property
    def user_controller(self) -> UserController:
        return self.__user_controller

    @property
    def producer_controller(self) -> ProducerController:
        return self.__producer_controller

    @property
    def affiliate_controller(self) -> AffiliateController:
        return self.__affiliate_controller

    @property
    def sale_controller(self) -> SaleController:
        return self.__sale_controller

    @property
    def course_controller(self) -> CourseController:
        return self.__course_controller

    def get_state_of_controller(self, controller_name: str):
        try:
            return self.__program_state[controller_name]
        except KeyError:
            return None

    def start(self):
        self.show_view()

    def __init_controllers(self):
        self.__user_controller = self.get_state_of_controller("user_controller")
        if self.__user_controller is None:
            self.__user_controller = UserController(self)

        self.__producer_controller = self.get_state_of_controller("producer_controller")
        if self.__producer_controller is None:
            self.__producer_controller = ProducerController(self)

        self.__affiliate_controller = self.get_state_of_controller("affiliate_controller")
        if self.__affiliate_controller is None:
            self.__affiliate_controller = AffiliateController(self)

        self.__sale_controller = self.get_state_of_controller("sale_controller")
        if self.__sale_controller is None:
            self.__sale_controller = SaleController(self)

        self.__course_controller = self.get_state_of_controller("course_controller")
        if self.__course_controller is None:
            self.__course_controller = CourseController(self)

    def exit(self):
        self.__program_state["user_controller"] = self.__user_controller
        self.__program_state["producer_controller"] = self.__producer_controller
        self.__program_state["affiliate_controller"] = self.__affiliate_controller
        self.__program_state["sale_controller"] = self.__sale_controller
        self.__program_state["course_controller"] = self.__course_controller

        self.__system_dao.add("program_state", self.__program_state)
        exit(0)

    def to_user_view(self):
        self.__user_controller.show_view()

    def to_sale_view(self):
        self.__sale_controller.show_view()

    def to_producer_view(self):
        self.__producer_controller.show_view()

    def to_affiliate_view(self):
        self.__affiliate_controller.show_view()

    def to_course_view(self):
        self.__course_controller.show_view()

    def show_view(self):
        options = {
            1: self.to_user_view,
            2: self.to_producer_view,
            3: self.to_affiliate_view,
            4: self.to_course_view,
            5: self.to_sale_view,
            0: self.exit
        }

        while True:
            chosen_option = self.__system_view.view_options()
            options[chosen_option]()