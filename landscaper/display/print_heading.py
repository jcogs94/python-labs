from helper.display import add_chars_to_line, add_spaces

# Heading for game, including title of game
def print_heading(line_len):
    lines = '=' * line_len
    title = ' LANDSCAPER '

    title_line = add_spaces(title)
    title_line = add_chars_to_line(line_len, title_line, '|')

    print(lines + '\n' + title_line + '\n' + lines)
