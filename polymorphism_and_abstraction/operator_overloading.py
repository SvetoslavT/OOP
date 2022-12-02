# Operator overloading
class Grades:
    def __init__(self, math: int, english: int):
        self.math = math
        self.english = english

    def __add__(self, other):
        grade_math = self.math + other.math
        grade_eng = self.english + other.english
        sum_grades = Grades(grade_math, grade_eng)
        return sum_grades


person1 = Grades(5, 3)
person2 = Grades(3, 6)
person3 = person1 + person2
print(person3.math)
print(person3.english)
