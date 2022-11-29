from wild_cat_zoo.animal import Animal


class Cheetah(Animal):

    def __init__(self, name: str, gender: str, age: int, money_for_care: int = 60):
        super().__init__(name, gender, age, money_for_care)
