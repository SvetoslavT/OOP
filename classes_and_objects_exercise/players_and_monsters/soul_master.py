from exercise.players_and_monsters.dark_wizzard import DarkWizzard


class SoulMaster(DarkWizzard):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __str__(self):
        return f"{self.username} of type {SoulMaster.__name__} has level {self.level}"