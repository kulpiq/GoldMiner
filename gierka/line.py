import pygame
import math

# Klasa reprezentująca linkę
class Linka:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.length = 35
        self.max_length = 450
        self.speed = 5
        self.angle = 0
        self.angle_speed = 1
        self.max_angle = 75
        self.direction_down = False
        self.moving = False
        self.caught_object = None  # Złapany obiekt

    def update(self):
        if not self.moving:
            self.angle += self.angle_speed
            if self.angle >= self.max_angle or self.angle <= -self.max_angle:
                self.angle_speed = -self.angle_speed
        
        if self.moving:
            if self.direction_down:
                self.length += self.speed

                # Jeśli złapaliśmy obiekt, natychmiast wracamy do góry
                if self.caught_object:
                    self.direction_down = False

                if self.length >= self.max_length:
                    self.direction_down = False

            else:
                self.length -= self.speed
                if self.length <= 35:
                    self.length = 35
                    self.moving = False
                    self.caught_object = None  # Obiekt zostaje uwolniony po dotarciu do góry

    def start_moving(self):
        self.moving = True
        self.direction_down = True

    def get_end_position(self):
        end_x = self.start_x + self.length * math.sin(math.radians(self.angle))
        end_y = self.start_y + self.length * math.cos(math.radians(self.angle))
        return end_x, end_y

    def check_collision(self, obj):
        end_x, end_y = self.get_end_position()
        if obj.rect.collidepoint(end_x, end_y):
            self.caught_object = obj  # Złap obiekt (kamień lub złoto)
            obj.caught = True  # Oznacz obiekt jako złapany

    def draw(self, screen):
        end_x, end_y = self.get_end_position()
        pygame.draw.line(screen, (0, 0, 0), (self.start_x, self.start_y), (end_x, end_y), 2)

        # Jeśli złapano obiekt, rysuj go przy końcu linki
        if self.caught_object:
            self.caught_object.rect.center = (end_x, end_y)
            self.caught_object.draw(screen)