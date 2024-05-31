import os
from game import Game

game_running = True
while game_running:
    os.system('clear')
    game = Game()
    game.print_heading()
    game.print_state()
    print(game.word)

    user_select = input('Enter a letter (q to quit): ')

    if user_select == 'q':
        game_running = False
