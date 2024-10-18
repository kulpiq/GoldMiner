import pygame
import math
import random
from stone import Stone
from stone2 import Stone2
from gold import Gold
from gold2 import Gold2
from gold3 import Gold3
from cashbag import Cashbag


class Linka:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.length = 35
        self.max_length = 460
        self.speed = 5
        self.angle = 0
        self.angle_speed = 1
        self.max_angle = 75
        self.direction_down = False
        self.moving = False
        self.caught_object = None
        self.base_speed = 5  
        self.speed = self.base_speed

    def update(self):
        if not self.moving:
            self.angle += self.angle_speed
            if self.angle >= self.max_angle or self.angle <= -self.max_angle:
                self.angle_speed = -self.angle_speed
        
        if self.moving:
            if self.direction_down:
                self.length += self.speed

                if self.caught_object:
                    self.direction_down = False

                if self.length >= self.max_length:
                    self.direction_down = False

            else:
                self.length -= self.speed
                if self.length <= 35:
                    self.length = 35
                    self.moving = False
                    self.caught_object = None  
                    self.speed = self.base_speed

    def start_moving(self):
        self.moving = True
        self.direction_down = True

    def reach_top(self):
        return self.length == 35 and not self.direction_down

    def get_end_position(self):
        end_x = self.start_x + self.length * math.sin(math.radians(self.angle))
        end_y = self.start_y + self.length * math.cos(math.radians(self.angle))
        return end_x, end_y
    


    def check_collision(self, obj):
        end_x, end_y = self.get_end_position()
        if obj.rect.collidepoint(end_x, end_y):
            self.caught_object = obj
            obj.caught = True
            
            if isinstance(obj, Stone):
                self.speed = self.base_speed / 2.5  
            elif isinstance(obj, Stone2):
                self.speed = self.base_speed / 1.5
            elif isinstance(obj, Gold):
                self.speed = self.base_speed / 3
            elif isinstance(obj, Gold3):
                self.speed = self.base_speed / 1.5
            elif isinstance(obj, Cashbag):
                self.speed = random.randint(1, 5)
            else:
                self.speef = self.base_speed

               

    def draw(self, screen):
        end_x, end_y = self.get_end_position()
        pygame.draw.line(screen, (0, 0, 0), (self.start_x, self.start_y), (end_x, end_y), 2)

    
        if self.caught_object:
            self.caught_object.rect.center = (end_x, end_y)
            self.caught_object.draw(screen)