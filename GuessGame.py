from time import sleep
import random

from Game import Game


class GuessGame(Game):

    def __init__(self, difficulty):
        super().__init__(difficulty)
        print("Generating a Number....")
        sleep(2)
        self.secret_number = self._generate_number()

    def _generate_number(self):
        # Will generate automatic random number
        secret_number = int(random.uniform(1, self.difficulty * 10))
        return secret_number

    def _get_guess_from_user(self):
        # The user will choose a number
        number = int(input(f"You need to guess a number between 1 to {self.difficulty *10}: "))
        return number

    def _compare_results(self, number):
        # checking if the number the user chose equal to the random number
        if self.secret_number == number:
            return True

    def play(self):
        # The start function, will start all functions and return false or true
        print(" The number is ready. Now it is Your turn")
        sleep(1)
        number = self._get_guess_from_user()
        if self._compare_results(number=number):
            return True
        else:
            return False
