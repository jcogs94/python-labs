import os
import print_game
from words import words


game_running = True
while game_running:
    os.system('clear')
    print_game.heading()
    print_game.state()

    user_select = input('Enter a letter (q to quit): ')

    if user_select == 'q':
        game_running = False
