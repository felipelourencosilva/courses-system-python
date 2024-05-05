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
            1: self.generate_report,
            0: self.previous_view
        }
        while True:
            chosen_option = self.__sale_view.view_options()
            options[chosen_option]()

    def generate_report(self):
        self.__sale_view.show_message("RELATÓRIO:")

        str = "Curso mais vendido: "
        most_sold_course = self.most_sold_course()
        if most_sold_course[0] is None:
            str += "Não houve nenhuma venda até o momento."
        else:
            str += most_sold_course[0].name + ", com um total de " + most_sold_course[1] + " vendas."
        self.__sale_view.show_message(str)

        str = "Curso com maior lucro: "
        course_with_most_profit = self.course_with_most_profit()
        if course_with_most_profit[0] is None:
            str += "Não houve nenhuma venda até o momento."
        else:
            str += course_with_most_profit[0].name + ", com um lucro total de $" + course_with_most_profit[1] + "."
        self.__sale_view.show_message(str)

        str = "Aluno com mais cursos: "
        user_with_most_courses = self.user_with_most_courses()
        if user_with_most_courses[0] is None:
            str += "Nenhum aluno comprou nenhum curso até o momento."
        else:
            str += user_with_most_courses[0].name + ", com um total de " + user_with_most_courses[1] + " cursos."
        self.__sale_view.show_message(str)

        str = "Produtor com mais vendas: "
        producer_with_most_sales = self.producer_with_most_sales()
        if producer_with_most_sales[0] is None:
            str += "Não houve nenhuma venda até o momento."
        else:
            str += producer_with_most_sales[0].name + ", com um total de " + producer_with_most_sales[1] + " vendas."
        self.__sale_view.show_message(str)

        str = "Afiliado com maior lucro: "
        affiliate_with_most_profit = self.affiliate_with_most_profit()
        if affiliate_with_most_profit[0] is None:
            str += "Não houve nenhuma venda comissionada até o momento."
        else:
            str += affiliate_with_most_profit[0].name + ", com um total de $" + affiliate_with_most_profit[1] + " em comissões."
        self.__sale_view.show_message(str)

    def add_sale(self, sale: Sale):
        if isinstance(sale, Sale):
            self.__sales.append(sale)

    def most_sold_course(self):
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

        return best

    def course_with_most_profit(self):
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

        return best

    def user_with_most_courses(self):
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

        return best

    def producer_with_most_sales(self):
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

        return best

    def affiliate_with_most_profit(self):
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

        return best
