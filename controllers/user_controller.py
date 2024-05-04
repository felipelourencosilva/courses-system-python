from views.user_view import UserView


class UserController:
    def __init__(self):
        self.__user_view = UserView()

    def show_view(self):
        self.__user_view.show_view()