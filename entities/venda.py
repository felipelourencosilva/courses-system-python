from user import *
from course import *
from affiliate import *


class Venda:
    def __init__(self, user: User, course: Course, affiliate: None):
        if isinstance(user, User):
            self.__user = user
        if isinstance(course, Course):
            self.__course = course

        self.__affiliate = None
        if isinstance(affiliate, Affiliate):
            self.__affiliate = affiliate

    @property
    def user(self) -> User:
        return self.__user

    @property
    def course(self) -> Course:
        return self.__course

    @property
    def affiliate(self) -> Affiliate:
        return self.__affiliate
