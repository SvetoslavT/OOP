class Vet:
    # Class attributes
    animals = []
    space = 5

    # Constructor method
    def __init__(self, name: str):
        self.name = name
        self.animals = []

    # Class method for adding animals if there is space
    def register_animal(self, animal_name: str):
        if Vet.space > 0:
            self.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    # Class method for releasing animals if they are in the clinic
    def unregister_animal(self, animal_name: str):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} is not in the clinic"

    # Class method for listing the vet and the animals he cares for
    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
