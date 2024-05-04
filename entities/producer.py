from user import *

class Producer(User):
    def __init__(self):
        super().__init__()
        print("Producer instantiated")


prod = Producer()