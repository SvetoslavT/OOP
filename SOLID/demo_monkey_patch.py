class A:
    @staticmethod
    def say_hello():
        print("Hey")


def say_bye():
    print("Bye")


obj_hi = A()
obj_hi.say_hello()
obj_hi.say_hello = say_bye
obj_hi.say_hello()
