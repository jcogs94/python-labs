from game_data import Game
from display.display_game import display_game

def get_input(prompt):
    print()
    user_input = input(prompt)
    return user_input

game = Game()
display_game(game)

while game.running:
    user_input = get_input('What would you like to do? ')

    if user_input == "1":
        print('store...')
    elif user_input == "2":
        print('Cutting grass...')
    elif user_input == "3":
        game.running = False
    else:
        print('Invalid input. Try again.')
