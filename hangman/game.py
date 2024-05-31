import random
from words import words
from methods.print_game import print_game


class Game:
    def word_init(self):
        self.word = (random.choice(words)).upper()
    
    def guess_str_init(self):
        str = ''
        for char in self.word:
            if char == '-':
                str += '-'
            else:
                str += ' '
        
        self.guess_str = str
    
    def new_game(self):
        self.word_init()
        self.guess_str_init()

    def display(self):
        print_game(self.guess_str, self.wins, self.losses)

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.new_game()

