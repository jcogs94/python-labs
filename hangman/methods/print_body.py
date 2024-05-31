from helpers.printing import add_spaces, calc_spaces, add_chars_to_line

margin_spaces = 4
margin_str = ' ' * margin_spaces

def new_line(line_len):
    print('|' + (' ' * (line_len - 2)) + '|')

def game_over_lines(line_len):
    game_over_str = add_spaces('GAME OVER')
    line = '|' + add_chars_to_line((line_len - 2), game_over_str, ' ') + '|'
    print(line)

def attempts_line(line_len, attempts):
    attempts_str = 'Attempts remaining: ' + str(attempts)
    line = '|' + add_chars_to_line((line_len - 2), attempts_str, ' ') + '|'
    print(line)

def play_and_win_line(line_len, guess_str, wins):
    line_left = '|' + margin_str + add_spaces(guess_str)
    line_right = 'Wins: ' + str(wins) + margin_str + '|'
    
    spacing = ' ' * calc_spaces(line_len, line_left, line_right)
    line = line_left + spacing + line_right

    print(line)

def under_and_loss_line(line_len, guess_str, losses):
    underlines = ''
    for char in guess_str:
        if char == '-':
            underlines += ' '
        else:
            underlines += '_'

    underlines = add_spaces(underlines)

    line_left = '|' + margin_str + underlines
    line_right = 'Losses: ' + str(losses) + margin_str + '|'
    
    spacing = ' ' * calc_spaces(line_len, line_left, line_right)
    line = line_left + spacing + line_right

    print(line)

def letters_guessed_line(line_len, letters_guessed):
    letters_str = 'Letters guessed:'
    for char in letters_guessed:
        letters_str += ' ' + char
    
    line = '|' + add_chars_to_line((line_len - 2), letters_str, ' ') + '|'
    print(line)

def print_body(line_len, guess_str, wins, losses, attempts, letters_guessed, game_over):
    new_line(line_len)
    
    if game_over:
        game_over_lines(line_len)
    else:
        attempts_line(line_len, attempts)
    
    letters_guessed_line(line_len, letters_guessed)
    new_line(line_len)

    play_and_win_line(line_len, guess_str, wins)
    under_and_loss_line(line_len, guess_str, losses)
    new_line(line_len)


    print(('=' * line_len) + '\n')
