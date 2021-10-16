import pygame
from settings import *

class Beam:
    def __init__(self, y):
        self.image = pygame.Surface((screen_width, 30))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = (0, y))
        self.draw = False
        self.draw_timeout = 0

    def update(self):
        if self.draw:
            self.draw_timeout += 1
            if self.draw_timeout < 4: self.image.set_alpha(255 / 4 * self.draw_timeout)
            else: self.image.set_alpha(255 - (255 / 4 * (self.draw_timeout - 4)))
            if self.draw_timeout > 8:
                self.draw_timeout = 0
                self.draw = False

    def show(self, display_screen):
        if self.draw:
            display_screen.blit(self.image, self.rect)
