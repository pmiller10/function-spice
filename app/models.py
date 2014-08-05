class Game:

    games = {}
    current_id = 0

    @classmethod
    def get(self, game_id):
        return self.games[game_id]

    def __init__(self):
        self.data = range(7);
        self.game_id = self.current_id
        self.games[self.game_id] = self
        self.current_id += 1

class Function:

    def __init__(self, function):
        y = []
        for i in range(7):
            y.append(eval(function, {'x': i}))
        self.data = y
