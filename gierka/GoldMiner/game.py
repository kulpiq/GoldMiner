import pygame
import random
from line import Linka
from gold import Gold
from stone import Stone
from gold2 import Gold2
from gold3 import Gold3
from stone2 import Stone2
from diamond import Diament
from mole import Kret
from molediamond import KretDiament
from cashbag import Cashbag


class Gra:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 800, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Gold Miner")
        self.clock = pygame.time.Clock()
        self.linka = Linka(self.screen_width // 2, 100)
        self.background_image = pygame.image.load('images/lvl_background.png')
        self.gold_objects = [Gold(400, 400), Gold2(200, 450), Gold3(600, 500)]
        self.stone_objects = [Stone(500, 300), Stone2(300, 350)]
        self.diamond_objects = [Diament(350, 300)]
        self.mole_objects = [Kret(100, 300), KretDiament(700, 400)]
        self.cashbag_objects = [Cashbag(200, 200), Cashbag(200, 300), Cashbag(200, 250)]  
        self.caught_object = None
        self.state = "start"
        self.start_button_rect = pygame.Rect(self.screen_width // 2 - 100, self.screen_height // 2 - 50, 200, 100)
        self.start_background = pygame.image.load("images/start_background.png")
        self.start_background = pygame.transform.scale(self.start_background, (self.screen_width, self.screen_height))

    def show_start_screen(self):
        self.screen.blit(self.start_background, (0, 0))
        pygame.draw.rect(self.screen, (195, 195, 195), self.start_button_rect)
        font = pygame.font.SysFont(None, 55)
        text = font.render("Start", True, (255, 255, 255))
        self.screen.blit(text, (self.screen_width // 2 - 50, self.screen_height // 2 - 25))
        pygame.display.flip()

    def check_collisions(self):
        for gold in self.gold_objects:
            if not gold.caught and self.linka.check_collision(gold):
                self.caught_object = gold
                gold.caught = True
                self.linka.catch_object(gold)

        for stone in self.stone_objects:
            if not stone.caught and self.linka.check_collision(stone):
                self.caught_object = stone
                stone.caught = True
                self.linka.catch_object(stone)
        
        for diamond in self.diamond_objects:
            if not diamond.caught and self.linka.check_collision(diamond):
                self.caught_object = diamond
                diamond.caught = True
                self.linka.catch_object(diamond)
        
        for mole in self.mole_objects:
            if not mole.caught and self.linka.check_collision(mole) and mole.visible:
                self.caught_object = mole
                mole.caught = True
                self.linka.catch_object(mole)
        
        for cashbag in self.cashbag_objects:
            if not cashbag.caught and self.linka.check_collision(cashbag) and cashbag.visible:
                self.caught_object = cashbag
                cashbag.caught = True
                self.linka.catch_object(cashbag)


    def update_caught_object(self):
        if self.caught_object:
            self.linka.pull_object(self.caught_object)
            

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.state == "start":
                    if self.start_button_rect.collidepoint(event.pos):
                        self.state = "playing"
                if event.type == pygame.KEYDOWN and self.state == "playing":
                    if event.key == pygame.K_DOWN and not self.linka.moving:
                        self.linka.start_moving()

            if self.state == "start":
                self.show_start_screen()
            elif self.state == "playing":
                self.linka.update()
                self.screen.blit(self.background_image, (0, 0))

                if self.linka.moving and self.linka.direction_down and not self.caught_object:
                    self.check_collisions()

                self.update_caught_object()

                self.linka.draw(self.screen)

                for gold in self.gold_objects:
                    if not gold.caught:
                        gold.draw(self.screen)

                for stone in self.stone_objects:
                    if not stone.caught:
                        stone.draw(self.screen)
                
                for diamond in self.diamond_objects:
                    if not diamond.caught:
                        diamond.draw(self.screen)

                for kret in self.mole_objects:
                    if not kret.caught:
                        kret.update() 
                        kret.draw(self.screen)

                for cashbag in self.cashbag_objects:
                    if not cashbag.caught:
                        cashbag.draw(self.screen)



                pygame.display.flip()  
                self.clock.tick(60)  

        pygame.quit()

if __name__ == "__main__":
    gra = Gra()
    gra.run()
