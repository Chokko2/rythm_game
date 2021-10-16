import pygame
from button import Button
from settings import *

class Level:
    def __init__(self, display_screen, font, background_music):
        self.background_music = background_music
        self.display_screen = display_screen
        self.buttons = pygame.sprite.Group()
        self.speed = 7
        self.round_score = 0 # The last rounds score
        self.font = font
        self.score = 0
        self.game_active = True
        background_music.play(loops=-1)

    def die(self):
        self.buttons.empty()
        self.game_active = False
        self.round_score = self.score
        self.score = 0
        self.speed = 7
        self.background_music.stop()

    def check_for_button(self, button_clicked):
        found_clickable = False

        if not self.game_active:
            self.game_active = True
            self.background_music.play(loops = -1)
            return
        elif self.game_active:
            for button in self.buttons:
                if button.clickable: found_clickable = True
            if not found_clickable and (
                button_clicked == pygame.K_h or
                button_clicked == pygame.K_l or
                button_clicked == pygame.K_k or
                button_clicked == pygame.K_l
            ):
                self.die()
            else: # if we found a button that is clickable
                for button in self.buttons:
                    if button.clickable:
                        if button_clicked == pygame.K_h and button.color == 'Red':
                            self.score += 1
                            self.speed += 0.1
                            button.kill()
                        elif button_clicked == pygame.K_j and button.color == 'Yellow':
                            self.score += 1
                            self.speed += 0.1
                            button.kill()
                        elif button_clicked == pygame.K_k and button.color == 'Green':
                            self.score += 1
                            self.speed += 0.1
                            button.kill()
                        elif button_clicked == pygame.K_l and button.color == 'Blue':
                            self.score += 1
                            self.speed += 0.1
                            button.kill()
                        else:
                            self.die()

    def run(self):
        if self.game_active:
            self.display_screen.fill((20, 20, 20))

            for i in range(0, screen_height, int(screen_height / 4)):
                pygame.draw.rect(self.display_screen, 'White', (screen_width-100, i  + screen_height / 12, 50, 50), 5)

            for button in self.buttons:
                alive = button.update(self.speed)
                if not alive:
                    self.die()
                    break

            self.buttons.draw(self.display_screen)

            score_surface = self.font.render(f'Score: {self.score}', True, 'White')
            score_rect = score_surface.get_rect(topleft = (20, 20))
            self.display_screen.blit(score_surface, score_rect)

        elif not self.game_active:
            self.display_screen.fill((150, 150, 150))

            round_score_surface = self.font.render(f'Score: {self.round_score}', True, 'White')
            round_score_rect = round_score_surface.get_rect(center = (screen_width / 2, screen_height / 2))
            self.display_screen.blit(round_score_surface, round_score_rect)
