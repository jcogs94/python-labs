import os
from display.print_heading import print_heading
from display.print_body import print_body

def display_game(game):
    line_len = 100

    os.system('clear')
    print_heading(line_len)
    print_body(line_len, game)
