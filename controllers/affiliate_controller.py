from views.affiliate_view import *


class AffiliateController:
    def __init__(self, system_controller):
        self.__affiliate_view = AffiliateView()
        self.__system_controller = system_controller

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            0: self.previous_view
        }
        self.__affiliate_view.show_view()