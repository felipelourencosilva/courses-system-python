from entities.affiliate import *
from entities.course import *
import copy


class Sale:
    def __init__(self, user: User, course: Course, affiliate: Affiliate = None):
        if isinstance(user, User):
            self.__user = copy.deepcopy(user)
        if isinstance(course, Course):
            self.__course = copy.deepcopy(course)

        self.__affiliate = None
        if isinstance(affiliate, Affiliate):
            self.__affiliate = copy.deepcopy(affiliate)

    @property
    def user(self) -> User:
        return self.__user

    @property
    def course(self) -> Course:
        return self.__course

    @property
    def affiliate(self) -> Affiliate:
        return self.__affiliate
