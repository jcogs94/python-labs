import os
from game import Game

game_running = True
while game_running:
    game = Game()
    game.display()

    user_select = input('Enter a letter (q to quit): ')

    if user_select == 'q':
        game_running = False
