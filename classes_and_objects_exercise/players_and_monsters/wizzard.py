from exercise.players_and_monsters.hero import Hero


class Wizzard(Hero):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)

    def __str__(self):
        return f"{self.username} of type {Wizzard.__name__} has level {self.level}"
