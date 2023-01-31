import abc


class Game(abc.ABC):

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def play(self):
        pass
