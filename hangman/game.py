import random
from words import words
from methods.print_game import print_game


class Game:
    def word_init(self):
        self.word = (random.choice(words)).upper()
    
    def guess_str_init(self):
        str = ''
        for char in self.word:
            if char == '-':
                str += '-'
            else:
                str += ' '
        
        self.guess_str = str
    
    def new_game(self):
        self.game_over = False
        self.attempts = 8
        self.letters_guessed = []
        self.word_init()
        self.guess_str_init()

    def display(self):
        print_game(self.guess_str, self.wins, self.losses,
            self.attempts, self.letters_guessed, self.game_over)
    
    def update_guess_str(self, letter):
        new_guess_str = ''
        for i in range(0, len(self.word)):
            if self.word[i] == '-':
                new_guess_str += '-'
            elif self.word[i] == letter:
                new_guess_str += letter
            elif self.guess_str[i] != ' ':
                new_guess_str += self.guess_str[i]
            else:
                new_guess_str += ' '
        
        self.guess_str = new_guess_str

    def check_for_win(self):
        if self.guess_str == self.word:
            self.wins += 1
        else:
            self.losses += 1

    def check_letter(self, letter):
        if letter in self.word:
            self.update_guess_str(letter)
        else:
            self.attempts -= 1
        
        self.letters_guessed.append(letter)

        if self.attempts > 0 and self.guess_str != self.word:
            self.display()
        else:
            self.game_over = True
            self.check_for_win()
            self.guess_str = self.word
            self.display()

    def __init__(self):
        self.running = True
        self.wins = 0
        self.losses = 0
        self.new_game()

