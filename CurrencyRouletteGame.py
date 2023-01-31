import random
import os
from currency_converter import CurrencyConverter

from Game import Game


class CurrencyRouletteGame(Game):

    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.usd, self.t, self.low, self.high = self.get_money_interval()

    def get_money_interval(self):

        c = CurrencyConverter()
        usd = int(random.uniform(1, 100))

        t = c.convert(usd, 'USD', 'ILS')
        low = int(t - (5 - self.difficulty))
        high = int(t + (5 - self.difficulty))
        return usd, t, low, high

    def get_guess_from_user(self):
        # User needs to guess the Value to a given amount of USD
        while True:
            try:
                guess = int(input(f"Guess the value of {self.usd}$ in ILS: "))
            except ValueError:
                print("Error: Enter just numbers please, not letters, words ,etc...")
                continue
            return guess

    def play(self):
        # Will call all other functions to start the game
        guess = self.get_guess_from_user()
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.high >= guess >= self.low:
            return True
        else:
            return False
