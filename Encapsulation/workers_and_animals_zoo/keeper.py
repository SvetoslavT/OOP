from wild_cat_zoo.worker import Worker


class Keeper(Worker):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age, salary)
