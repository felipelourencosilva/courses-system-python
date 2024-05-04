from views.system_view import *
from controllers.user_controller import *
from controllers.sale_controller import *


class SystemController:

    def __init__(self):
        self.__user_controller = UserController()
        self.__sale_controller = SaleController()
        self.__system_view = SystemView()

    @property
    def user_controller(self) -> UserController:
        return self.__user_controller

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

    def show_view(self):
        options = {
            0: self.exit
        }

        while True:
            chosen_option = self.__system_view.show_options()
            options[chosen_option]()