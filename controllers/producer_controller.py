from views.producer_view import *


class ProducerController:
    def __init__(self, system_controller):
        self.__producer_view = ProducerView()
        self.__system_controller = system_controller

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            0: self.previous_view
        }
        self.__producer_view.view_options()