from tools import tools
from display.display_game import display_game

class Game:
    def display(self):
        display_game(self)
    
    def cut_grass(self):
        total_earned = 0
        for tool in self.tools:
            tool_total = self.tools[tool]['earnings'] * self.tools[tool]['owned']
            total_earned += tool_total
        
        if total_earned == 0:
            total_earned = 1
        
        self.money += total_earned
        self.display()
    
    def __init__(self):
        self.running = True
        self.money = 0
        self.win_amount = 10
        self.tools = tools
        self.display()
        # self.new_game()