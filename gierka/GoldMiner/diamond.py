import pygame

class Diament:
    def __init__(self, x, y):
        self.image = pygame.image.load('images/diamond.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.caught = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)