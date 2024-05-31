import os
from game import Game

def get_input():
    return input("Guess a letter ('/' to quit): ")


game = Game()
game.display()

while game.running:
    user_select = get_input()
    user_select = user_select.upper()

    if user_select == '/':
        game.running = False
    elif len(user_select) > 1:
        print('Please choose only one letter.\n')
    elif user_select[0].isalpha():
        if user_select in game.letters_guessed:
            print(user_select + ' has already been guessed.\n')
        else:
            game.check_letter(user_select)
    else:
        print('Please enter a valid character.\n')
