from views.sale_view import *
from entities.sale import *


class SaleController:
    def __init__(self, system_controller):
        self.__sales = []
        self.__sale_view = SaleView()
        self.__system_controller = system_controller

    def previous_view(self):
        self.__system_controller.show_view()

    def show_view(self):
        options = {
            1: self.generate_full_report,
            2: self.show_most_sold_course,
            3: self.show_course_with_most_profit,
            4: self.show_user_with_most_courses,
            5: self.show_producer_with_most_sales,
            6: self.show_affiliate_with_most_profit,
            0: self.previous_view
        }
        while True:
            chosen_option = self.__sale_view.view_options()
            options[chosen_option]()

    def generate_full_report(self):
        self.show_most_sold_course()
        self.show_course_with_most_profit()
        self.show_user_with_most_courses()
        self.show_producer_with_most_sales()
        self.show_affiliate_with_most_profit()

    def add_sale(self, sale: Sale):
        if isinstance(sale, Sale):
            self.__sales.append(sale)

    def show_most_sold_course(self):
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
            str += best[0].name + ", com um total de " + best[1] + " vendas."
        self.__sale_view.show_message(str)

    def show_course_with_most_profit(self):
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
            str += best[0].name + ", com um lucro total de $" + best[1] + "."
        self.__sale_view.show_message(str)

    def show_user_with_most_courses(self):
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

        str = "Aluno com mais cursos: "
        if best[0] is None:
            str += "Nenhum aluno comprou nenhum curso até o momento."
        else:
            str += best[0].name + ", com um total de " + best[1] + " cursos."
        self.__sale_view.show_message(str)

    def show_producer_with_most_sales(self):
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
            str += best[0].name + ", com um total de " + best[1] + " vendas."
        self.__sale_view.show_message(str)

    def show_affiliate_with_most_profit(self):
        counter = {}
        for sale in self.__sales:
            if sale.affiliate is not None:
                if sale.course.affiliate not in counter:
                    counter[sale.course.affiliate] = 1
                counter[sale.course.producer] += 1

        best = [None, 0]
        for key in counter:
            if counter[key] >= best[1]:
                best[0] = key
                best[1] = counter[key]

        str = "Afiliado com maior lucro: "
        if best[0] is None:
            str += "Não houve nenhuma venda comissionada até o momento."
        else:
            str += best[0].name + ", com um total de $" + best[1] + " em comissões."
        self.__sale_view.show_message(str)
