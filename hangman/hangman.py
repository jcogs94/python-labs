import os
from game import Game

def get_input(game_over):
    if game_over:
        return input("Would you like to play again (y/n)? ")
    else:
        return input("Guess a letter ('/' to quit): ")


game = Game()
game.display()

while game.running:
    user_select = get_input(game.game_over)
    user_select = user_select.upper()
    
    if game.game_over:
        if user_select == 'Y':
            game.new_game()
            game.display()
        elif user_select == 'N':
            game.running = False
        else:
            print('Please enter a valid character.\n')
    else:
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
