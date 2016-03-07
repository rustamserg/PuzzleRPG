#!/usr/bin/env python
import pygame

import globals
from hex_map import HexMap
from layers.ai_layer import AILayer
from layers.ground_layer import GroundLayer
from layers.player_layer import PlayerLayer
from layers.ui_layer import UILayer
from world import World

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
world = World(background, hex_map, pygame.Rect(0, 0, globals.VIEW_WIDTH, globals.VIEW_HEIGHT))

world.add_layer(GroundLayer(hex_map))
world.add_layer(PlayerLayer(hex_map))
world.add_layer(UILayer())
world.add_layer(AILayer())

world.init()
world.start()

while not done:

    clock.tick(60)
    background.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            world.on_click(pos)

    world.update()
    world.draw()

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
