from views.sale_view import *
from entities.sale import *


class SaleController:
    __instance = None

    def __init__(self, system_controller):
        self.__sales = []
        self.__sale_view = SaleView()
        self.__system_controller = system_controller

    def __new__(cls, *args, **kwargs):
        if SaleController.__instance is None:
            SaleController.__instance = super(SaleController, cls).__new__(cls)
        return SaleController.__instance

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            1: self.generate_full_report,
            2: self.show_most_sold_course,
            3: self.show_course_with_most_profit,
            4: self.show_user_with_most_courses,
            5: self.show_producer_with_most_sales,
            6: self.show_producer_with_most_profit,
            7: self.show_affiliate_with_most_sales,
            8: self.show_affiliate_with_most_profit,
            0: self.previous_view
        }
        while True:
            chosen_option = self.__sale_view.view_options()
            options[chosen_option]()

    def generate_full_report(self):
        messages = [
            self.get_most_sold_course(),
            self.get_course_with_most_profit(),
            self.get_user_with_most_courses(),
            self.get_producer_with_most_sales(),
            self.get_producer_with_most_profit(),
            self.get_affiliate_with_most_sales(),
            self.get_affiliate_with_most_profit()
        ]
        self.__sale_view.show_complete_report(messages)

    def add_sale(self, user, course, affiliate=None):
        self.__sales.append(Sale(user, course, affiliate))

    def get_most_sold_course(self):
        counter = {}
        for sale in self.__sales:
            if sale.course not in counter:
                counter[sale.course] = 0
            counter[sale.course] += 1

        best = [None, 0]
        for key in counter:
            if counter[key] >= best[1]:
                best[0] = key
                best[1] = counter[key]

        str = "Curso mais vendido: "
        if best[0] is None:
            str += "Não houve nenhuma venda até o momento."
        else:
            str += f"{best[0].name}, com um total de {best[1]} venda(s)."
        return str

    def show_most_sold_course(self):
        self.__sale_view.show_single_report(
            self.get_most_sold_course()
        )

    def get_course_with_most_profit(self):
        counter = {}
        for sale in self.__sales:
            if sale.course not in counter:
                counter[sale.course] = 0
            counter[sale.course] += sale.course.price

        best = [None, 0]
        for key in counter:
            if counter[key] >= best[1]:
                best[0] = key
                best[1] = counter[key]

        str = "Curso com maior lucro: "
        if best[0] is None:
            str += "Não houve nenhuma venda até o momento."
        else:
            str += f"{best[0].name}, com um lucro total de ${best[1]}."
        return str

    def show_course_with_most_profit(self):
        self.__sale_view.show_single_report(
            self.get_course_with_most_profit()
        )

    def get_user_with_most_courses(self):
        counter = {}
        for sale in self.__sales:
            if sale.user not in counter:
                counter[sale.user] = 0
            counter[sale.user] += 1

        best = [None, 0]
        for key in counter:
            if counter[key] >= best[1]:
                best[0] = key
                best[1] = counter[key]

        str = "Usuário com mais cursos: "
        if best[0] is None:
            str += "Nenhum usuário comprou nenhum curso até o momento."
        else:
            str += f"{best[0].name} {best[0].surname}, com um total de {best[1]} curso(s)."
        return str

    def show_user_with_most_courses(self):
        self.__sale_view.show_single_report(
            self.get_user_with_most_courses()
        )

    def get_producer_with_most_sales(self):
        counter = {}
        for sale in self.__sales:
            if sale.course.producer not in counter:
                counter[sale.course.producer] = 0
            counter[sale.course.producer] += 1

        best = [None, 0]
        for key in counter:
            if counter[key] >= best[1]:
                best[0] = key
                best[1] = counter[key]

        str = "Produtor com mais vendas: "
        if best[0] is None:
            str += "Não houve nenhuma venda até o momento."
        else:
            str += f"{best[0].name} {best[0].surname}, com um total de {best[1]} venda(s)."
        return str

    def show_producer_with_most_sales(self):
        self.__sale_view.show_single_report(
            self.get_producer_with_most_sales()
        )

    def get_producer_with_most_profit(self):
        counter = {}
        for sale in self.__sales:
            if sale.course.producer not in counter:
                counter[sale.course.producer] = 0
            counter[sale.course.producer] += sale.course.price
            if sale.affiliate is not None:
                counter[sale.course.producer] -= sale.course.commission_price

        best = [None, 0]
        for key in counter:
            if counter[key] >= best[1]:
                best[0] = key
                best[1] = counter[key]

        str = "Produtor com maior lucro: "
        if best[0] is None:
            str += "Não houve nenhuma venda até o momento."
        else:
            str += f"{best[0].name} {best[0].surname}, com um lucro total de ${best[1]}."
        return str

    def show_producer_with_most_profit(self):
        self.__sale_view.show_single_report(
            self.get_producer_with_most_profit()
        )

    def get_affiliate_with_most_sales(self):
        counter = {}
        for sale in self.__sales:
            if sale.affiliate is not None:
                if sale.affiliate not in counter:
                    counter[sale.affiliate] = 0
                counter[sale.affiliate] += 1

        best = [None, 0]
        for key in counter:
            if counter[key] >= best[1]:
                best[0] = key
                best[1] = counter[key]

        str = "Afiliado com mais vendas: "
        if best[0] is None:
            str += "Não houve nenhuma venda comissionada até o momento."
        else:
            str += f"{best[0].name} {best[0].surname}, com um total de {best[1]} venda(s)."
        return str

    def show_affiliate_with_most_sales(self):
        self.__sale_view.show_single_report(
            self.get_affiliate_with_most_sales()
        )

    def get_affiliate_with_most_profit(self):
        counter = {}
        for sale in self.__sales:
            if sale.affiliate is not None:
                if sale.affiliate not in counter:
                    counter[sale.affiliate] = 0
                counter[sale.affiliate] += sale.course.commission_price

        best = [None, 0]
        for key in counter:
            if counter[key] >= best[1]:
                best[0] = key
                best[1] = counter[key]

        str = "Afiliado com maior lucro: "
        if best[0] is None:
            str += "Não houve nenhuma venda comissionada até o momento."
        else:
            str += f"{best[0].name} {best[0].surname}, com um total de ${best[1]} em comissões."
        return str

    def show_affiliate_with_most_profit(self):
        self.__sale_view.show_single_report(
            self.get_affiliate_with_most_profit()
        )
