class Animal:
    def eat(self):
        return "eating..."


class Dog(Animal):
    def bark(self):
        return "barking..."


dog = Dog()
print(dog.eat())
print(dog.bark())
