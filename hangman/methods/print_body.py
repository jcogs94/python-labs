from helpers.printing import add_spaces, calc_spaces, add_chars_to_line

margin_spaces = 4
margin_str = ' ' * margin_spaces

def new_line(line_length):
    print('|' + (' ' * (line_length - 2)) + '|')

def attempts_line(line_len):
    attempts_str = 'Attempts remaining: 8'
    
    line = '|' + add_chars_to_line((line_len - 2), attempts_str, ' ') + '|'
    print(line)

def play_and_win_line(line_len, word):
    line_left = '|' + margin_str + add_spaces(word)
    line_right = 'Wins: 0' + margin_str + '|'
    
    spacing = ' ' * calc_spaces(line_len, line_left, line_right)
    line = line_left + spacing + line_right

    print(line)

def under_and_loss_line(line_len, word):
    underlines = ''
    for char in word:
        if char == '-':
            underlines += ' '
        else:
            underlines += '_'

    underlines = add_spaces(underlines)

    line_left = '|' + margin_str + underlines
    line_right = 'Losses: 0' + margin_str + '|'
    
    spacing = ' ' * calc_spaces(line_len, line_left, line_right)
    line = line_left + spacing + line_right

    print(line)

def print_body(line_len, word):
    new_line(line_len)
    attempts_line(line_len)

    play_and_win_line(line_len, word)
    under_and_loss_line(line_len, word)
    new_line(line_len)

    print(('=' * line_len) + '\n')
