import random
from words import words
from methods.print_game import print_game


class Game:
    def __init__(self):
        self.word = (random.choice(words)).upper()

    def display(self):
        print_game(self.word)
