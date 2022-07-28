from player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):

        if player in self.players:
            return f"Player {player} is already in the guild."
        if player.guild != 'Unaffiliated':
            return f"Player {player} is in another guild."
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player):
        player.guild = 'Unaffiliated'
        return f"Player {player} has been removed from the guild."

    def guild_info(self):
        return f'''
    Guild: {self.name}
    Players: {[player.name for player in self.players]}
        '''
