import os
import math

def heading_str():
    line_len = 60
    lines = '=' * line_len

    title = 'HANGMAN'
    num_side_equals = line_len - len(title) - 2
    
    left_side_equals = ''
    right_side_equals = ''
    if num_side_equals % 2 == 0:
        left_side_equals = '=' * (num_side_equals / 2)
        right_side_equals = left_side_equals
    else:
        left_side_equals = '=' * math.ceil(num_side_equals / 2)
        right_side_equals = '=' * math.floor(num_side_equals / 2)
    
    title = left_side_equals + ' ' + title + ' ' + right_side_equals

    print(lines)
    print(title)
    print(lines)

game_running = True

while game_running:
    os.system('clear')
    heading_str()
    print('New game...')
    user_select = input('Enter a letter (q to quit): ')

    if user_select == 'q':
        game_running = False
