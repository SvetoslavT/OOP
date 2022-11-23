# SINGLE INHERITANCE
#
# class Parent:
#     def say_something(self):
#         return "What's up?"
#
#
# class Child(Parent):
#     def answer(self):
#         return "Everything's fine!"
#
#
# person1 = Parent()
# person2 = Child()
#
# print(person1.say_something())
# print(person2.say_something())
# print(person2.answer())

# MULTIPLE INHERITANCE

class Father:
    def __init__(self):
        self.father_name = "Radoslav Trifonov"


class Mother:
    def __init__(self):
        self.mother_name = "Bistra Trifonova"


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parents_info(self):
        return f"Mother: {self.mother_name}\nFather: {self.father_name}"

person1 = Child()
print(person1.get_parents_info())