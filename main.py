#!/usr/bin/env python
import pygame

import globals
from core.hex_map import HexMap
from game import Game

black = pygame.Color(0, 0, 0)

pygame.init()

size = [globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("HEX")

done = False
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background = background.convert()

hex_map = HexMap(globals.WORLD_WIDTH, globals.WORLD_HEIGHT)
game = Game(background, hex_map)

game.init()
game.start()

while not done:

    clock.tick(60)
    background.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            game.on_click(pos)

    game.update()
    game.draw()

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
