from tools import tools

class Game:
    def __init__(self):
        self.running = True
        self.money = 0
        self.win_amount = 10
        self.tools = tools
        # self.new_game()