import string
import time
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score

CHOSEN_GAME = {
    1: GuessGame,
    2: MemoryGame,
    3: CurrencyRouletteGame
}


def _welcome():
    name = input('Hi - What is your Name? ')
    print(f'Hello {name} and welcome to the World of Games (WoG) \n Here you can find many cool games to play.')
    return name


def _number_of_tries(difficulty: int) -> int:
    return (6 - difficulty) * 2


def load_game():
    time.sleep(1)
    print(""" Please choose a game to play:
        1. Guess Game - guess a number and see if you chose like the computer
        2. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        After game choice selection  -  you will choose the Game difficulty from 1 to 5 """)
    time.sleep(1)

    game = read_digit(1, 3, 'Choose a game from above list ')
    difficulty = read_digit(1, 5, 'Choose Difficulty')
    num_tries = _number_of_tries(difficulty)

    game = CHOSEN_GAME[game](difficulty)

    for i in range(num_tries):
        result = game.play()
        if result:
            print(' Nice, you have Won')
            add_score(difficulty=difficulty)
            time.sleep(1)
            break
        elif i < num_tries - 1:
            print(f' Failed - Try again. You have {num_tries - i - 1} tries left.')
        else:
            print(' Game Over')


def read_digit(min_val: int, max_val: int, txt: string):
    while True:
        res = input(f'Please {txt} - between {min_val} - {max_val}: ')
        if res.isdigit() and min_val <= int(res) <= max_val:
            return int(res)
        else:
            print(f'Hay: {res}  is an Error- enter a number choice between {min_val}-{max_val} - no letters or symbols')
