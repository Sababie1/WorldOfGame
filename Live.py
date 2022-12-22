import string
import time
import GuessGame
import MemoryGame
import CurrencyRouletteGame
from Score import add_score

CHOSEN_GAME = {
    1: GuessGame.play,
    2: MemoryGame.play,
    3: CurrencyRouletteGame.play
}


def _welcome():
    name = input('Hi - What is your Name? ')
    print(f'Hello {name} and welcome to the World of Games (WoG) \n Here you can find many cool games to play.')
    return name


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

    result = CHOSEN_GAME[game](difficulty)
    if result:
        print(' Nice, you have Won')
        add_score(difficulty=difficulty)
    else:
        print(' Failed - start the game again ')


def read_digit(min_val: int, max_val: int, txt: string):
    while True:
        res = input(f'Please {txt} - between {min_val} - {max_val}: ')
        if res.isdigit() and min_val <= int(res) <= max_val:
            return int(res)
        else:
            print(f'Hay: {res}  is an Error- enter a number choice between {min_val}-{max_val} - no letters or symbols')
