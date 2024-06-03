from helper.display import new_line, calc_spaces

margin_spaces = 4
margin_str = ' ' * margin_spaces
left_margin = '|' + margin_str
right_margin = margin_str + '|'

def tools_and_money(line_len, game):
    left_str = left_margin + 'Current tools:'
    right_str = 'Money: $' + str(game.money) + right_margin
    print(left_str + (' ' * calc_spaces(line_len, left_str, right_str)) + right_str)
    
    # print(game.tools)
    for tool in game.tools:
        earnings_per_day = game.tools[tool]['earnings'] * game.tools[tool]['owned']
        left_str = left_margin + '  > ' + tool + ' ($' + str(earnings_per_day) + '/day): ' + str(game.tools[tool]['owned'])
        right_str = (' ' * calc_spaces(line_len, left_str, right_margin)) + right_margin
        print(left_str + right_str)

def game_choice(line_len):
    left_str = left_margin + 'Choose what to do:'
    right_str = (' ' * calc_spaces(line_len, left_str, right_margin)) + right_margin
    print(left_str + right_str)

    left_str = left_margin + '  1. Tool shop'
    right_str = (' ' * calc_spaces(line_len, left_str, right_margin)) + right_margin
    print(left_str + right_str)

    left_str = left_margin + '  2. Cut grass for the day'
    right_str = (' ' * calc_spaces(line_len, left_str, right_margin)) + right_margin
    print(left_str + right_str)

    left_str = left_margin + '  3. Quit'
    right_str = (' ' * calc_spaces(line_len, left_str, right_margin)) + right_margin
    print(left_str + right_str)

def footer(line_len):
    new_line(line_len)
    print('=' * line_len)

def print_body(line_len, game):
    new_line(line_len)
    tools_and_money(line_len, game)
    new_line(line_len)
    game_choice(line_len)
    footer(line_len)
