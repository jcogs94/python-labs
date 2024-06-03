import math

def add_chars_to_line(line_len, str, add_char):
    chars_to_add = line_len - len(str)

    if chars_to_add % 2 == 0:
        chars = add_char * int((chars_to_add / 2))
        return chars + str + chars
    else:
        left_chars = add_char * math.ceil(chars_to_add / 2)
        right_chars = add_char * math.floor(chars_to_add / 2)
        return left_chars + str + right_chars

def add_spaces(str):
    new_str = ''
    for char in str:
        new_str += char + ' '
    
    return_str = ''
    for i in range(0, (len(new_str) - 1)):
        return_str += new_str[i]

    return return_str

def calc_spaces(line_len, line_left, line_right):
    return line_len - len(line_left) - len(line_right)

def new_line(line_len):
    print('|' + (' ' * (line_len - 2)) + '|')
