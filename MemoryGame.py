import time
import os

from Game import Game


class MemoryGame(Game):

    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.random_numbers = self._generate_sequence(difficulty)

    @staticmethod
    def _generate_sequence(difficulty):
        # Generate 5 Random numbers, creates a list and prints it
        import random
        random_numbers = []
        for number in range(difficulty):
            random_numbers.append(int(random.uniform(1, 101)))
        print(random_numbers, end='', flush=True)
        time.sleep(2)
        print('\r                                 ')
        os.system('cls')
        return random_numbers

    def _get_list_from_user(self):
        # The user choose 5 numbers
        user_numbers = []
        print(f"Please Insert {self.difficulty} numbers")
        for i in range(self.difficulty):
            i = user_numbers.append(int(input("Import a Number: ")))
        return user_numbers

    def _is_list_equal(self, user_numbers):
        # Checking if the lists are equal
        self.random_numbers.sort()
        user_numbers.sort()
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.random_numbers == user_numbers:
            return True
        else:
            return False

    def play(self):
        # The start function, will start all functions and return false or true
        user_numbers = self._get_list_from_user()
        if self._is_list_equal(user_numbers=user_numbers):
            return True
        else:
            return False
