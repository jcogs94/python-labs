from helpers.printing import add_spaces, add_chars_to_line

# Heading for game, including title of game
def print_heading(line_len):
    lines = '=' * line_len
    title = ' HANGMAN '

    title_line = add_spaces(title)
    title_line = add_chars_to_line(line_len, title_line, '|')

    print(lines + '\n' + title_line + '\n' + lines)
