import os
from methods.print_heading import print_heading
from methods.print_body import print_body

def print_game(word):
    line_len = 100

    os.system('clear')
    print_heading(line_len)
    print_body(line_len, word)
