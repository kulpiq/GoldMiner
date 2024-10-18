import pygame

class MoneyCounter:
    def __init__(self):
        self.amount = 0
    
    def add_money(self, amount):
        self.amount += amount
    
    def draw(self, screen):
        font = pygame.font.SysFont(None, 26)
        text = font.render(f'Money: ${self.amount}', True, (0, 0, 0))
        screen.blit(text, (25, 20))
