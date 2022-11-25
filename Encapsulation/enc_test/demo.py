class Person():
    def __init__(self, name, user_id):
        self.name = name
        self.__id = user_id

    def get_person_info(self):
        return f"Person: {self.name} with id {self.__id}"

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id
        return f"New id set for user: {self.name}"


person1 = Person("jordan", 123214)
print(person1.get_person_info())
print(person1.get_id())
print(person1.set_id(441123))
print(person1.get_id())
