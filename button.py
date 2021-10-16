import pygame
from settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self, y_pos):
        super().__init__()

        self.clickable = False

        self.image = pygame.Surface((50, 50))

        self.y_pos = y_pos
        self.color = 'Black'
        # Fill the image based on where the button is
        if y_pos == 0: self.color = 'Red'
        elif y_pos == 1: self.color = 'Yellow'
        elif y_pos == 2: self.color = 'Green'
        elif y_pos == 3: self.color = 'Blue'
        self.image.fill(self.color)

        self.rect = self.image.get_rect(topleft = (-50, y_pos * screen_height / 4 + screen_height / 12))

    def update(self, speed):
        self.rect.x += speed

        if self.rect.right > screen_width - 100 and self.rect.left < screen_width - 50:
            self.clickable = True
        else: self.clickable = False

        if self.rect.left > screen_width: self.kill()

        if self.rect.left > screen_width:
            return False

        return True
