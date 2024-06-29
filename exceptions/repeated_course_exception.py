class RepeatedCourseException(Exception):

    def __init__(self, msg: str = None):
        if msg is None:
            msg = "Esse usuário já possui esse curso."
        super().__init__(msg)
