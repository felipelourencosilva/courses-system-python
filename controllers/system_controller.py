from views.system_view import *
from controllers.user_controller import *
from controllers.producer_controller import *
from controllers.affiliate_controller import *
from controllers.sale_controller import *
from controllers.course_controller import *


class SystemController:

    def __init__(self):
        self.__user_controller = UserController(self)
        self.__producer_controller = ProducerController(self)
        self.__affiliate_controller = AffiliateController(self)
        self.__sale_controller = SaleController(self)
        self.__course_controller = CourseController(self)
        self.__system_view = SystemView()

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

    def start(self):
        self.show_view()

    def exit(self):
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