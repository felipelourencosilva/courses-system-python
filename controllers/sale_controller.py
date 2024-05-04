from views.sale_view import *


class SaleController:
    def __init__(self, system_controller):
        self.__sale_view = SaleView()
        self.__system_controller = system_controller

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            0: self.previous_view
        }
        self.__sale_view.view_options()