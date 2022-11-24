from exercise.players_and_monsters.wizzard import Wizzard


class DarkWizzard(Wizzard):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)

    def __str__(self):
        return f"{self.username} of type {DarkWizzard.__name__} has level {self.level}"
