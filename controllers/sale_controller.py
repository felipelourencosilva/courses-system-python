from views.sale_view import SaleView

class SaleController:
    def __init__(self):
        self.__sale_view = SaleView()

    def show_view(self):
        self.__sale_view.show_view()