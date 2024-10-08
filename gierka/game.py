import pygame
from line import Linka  
from gold import Gold  
from stone import Stone  
from gold2 import Gold2
from gold3 import Gold3
from stone2 import Stone2


class Gra:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 800, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Gold Miner")
        self.clock = pygame.time.Clock()
        self.linka = Linka(self.screen_width // 2, 200)
        
        # Obiekty złota i kamieni
        self.gold_objects = [Gold(400, 400), Gold2(200, 450), Gold3(600, 500)]
        self.stone_objects = [Stone(500, 300), Stone2(300, 350)]  # Lista kamieni

        # Złapany obiekt
        self.caught_object = None

        # Ekran startowy
        self.state = "start"  # Początkowy stan gry: ekran startowy
        self.start_button_rect = pygame.Rect(self.screen_width // 2 - 100, self.screen_height // 2 - 50, 200, 100)  # Guzik startu

        self.start_background = pygame.image.load("images\start_background.png")
        self.start_background = pygame.transform.scale(self.start_background, (self.screen_width, self.screen_height))

    def show_start_screen(self):
        # Ustawianie tła początkowego
        self.screen.blit(self.start_background, (0, 0))
        
        # Rysowanie przycisku start
        pygame.draw.rect(self.screen, (195, 195, 195), self.start_button_rect)
        
        # Tekst na przycisku
        font = pygame.font.SysFont(None, 55)
        text = font.render("Start", True, (255, 255, 255))
        self.screen.blit(text, (self.screen_width // 2 - 50, self.screen_height // 2 - 25))
        
        # Aktualizacja ekranu
        pygame.display.flip()

    def check_collisions(self):
        # Sprawdzamy kolizje linki ze złotem
        for gold in self.gold_objects:
            if not gold.caught and self.linka.check_collision(gold):
                self.caught_object = gold
                gold.caught = True
                self.linka.catch_object(gold)

        # Sprawdzamy kolizje linki z kamieniem
        for stone in self.stone_objects:
            if not stone.caught and self.linka.check_collision(stone):
                self.caught_object = stone
                stone.caught = True
                self.linka.catch_object(stone)

    def update_caught_object(self):
        # Jeśli linka złapała obiekt, to go podciąga
        if self.caught_object:
            self.linka.pull_object(self.caught_object)
            if self.linka.reached_top():  # Kiedy obiekt zostanie wciągnięty do góry
                self.caught_object = None  # Obiekt zostaje zwolniony

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.state == "start":
                    if self.start_button_rect.collidepoint(event.pos):
                        self.state = "playing"  # Zmieniamy stan na "playing", czyli zaczynamy grę

                if event.type == pygame.KEYDOWN and self.state == "playing":
                    if event.key == pygame.K_DOWN and not self.linka.moving:
                        self.linka.start_moving()

            # Wywołanie odpowiedniego stanu gry
            if self.state == "start":
                self.show_start_screen()  # Wywołanie ekranu startowego
            elif self.state == "playing":
                self.linka.update()

                # Sprawdzanie kolizji tylko, gdy linka idzie w dół
                if self.linka.moving and self.linka.direction_down and not self.caught_object:
                    self.check_collisions()
                
                # Aktualizowanie złapanego obiektu
                self.update_caught_object()
                
                # Rysowanie gry (linka, złoto, itp.)
                self.screen.fill((255, 255, 255))
                pygame.draw.line(self.screen, (200, 200, 200), (0, self.linka.start_y), (self.screen_width, self.linka.start_y), 2)
                self.linka.draw(self.screen)
                
                # Rysowanie złota i kamieni
                for gold in self.gold_objects:
                    if not gold.caught:  
                        gold.draw(self.screen)
                for stone in self.stone_objects:
                    if not stone.caught:
                        stone.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    gra = Gra()
    gra.run()