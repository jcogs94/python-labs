from game_data import Game
from display.display_game import display_game

game = Game()
display_game(game)

while game.running:
    game.running = False
