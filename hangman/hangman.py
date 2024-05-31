import os
from game import Game

def get_input():
    return input("Guess a letter ('/' to quit): ")


game = Game()
game.display()

while game.running:
    user_select = get_input()

    if user_select == '/':
        game.running = False
    elif len(user_select) > 1:
        print('Please choose only one letter.\n')
