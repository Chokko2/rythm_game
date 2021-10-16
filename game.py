from sys import exit
import pygame
from level import Level
from settings import *
from button import Button
from random import randint

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rythm Game')
clock = pygame.time.Clock()

font = pygame.font.Font('font/Pixeltype.ttf', 50)

# set our music
background_music = pygame.mixer.Sound('audio/music.wav')
background_music.set_volume(0.2)

level = Level(screen, font, background_music)

create_button = pygame.USEREVENT + 1
pygame.time.set_timer(create_button, 500)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == create_button:
			level.buttons.add(Button(randint(0, 3)))
		elif event.type == pygame.KEYDOWN:
			level.check_for_button(event.key)

	level.run()

	pygame.display.update()
	clock.tick(30)
