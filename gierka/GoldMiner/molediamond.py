import pygame

class KretDiament:
    def __init__(self, x, y):
        self.image = pygame.image.load('images/kretdiamond.png')  
        self.rect = self.image.get_rect(topleft=(x, y)) 
        self.speed = 1.45
        self.direction = 1  
        self.left_boundary = x - 70 
        self.right_boundary = x + 70  
        self.caught = False  

    def update(self):
        if not self.caught: 
            self.rect.x += self.speed * self.direction
            if self.rect.x <= self.left_boundary or self.rect.x >= self.right_boundary:
                self.direction *= -1
                self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, screen):
        screen.blit(self.image, self.rect)