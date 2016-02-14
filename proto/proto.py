#!/usr/bin/env python
import pygame
from hex_map import HexMap
from map_view import MapView
from player import Player
import globals

black = pygame.Color(0, 0, 0)

pygame.init()

size = [500, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("HEX")

done = False
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background = background.convert()

hex_map = HexMap(globals.WORLD_WIDTH, globals.WORLD_HEIGHT)
map_view = MapView(background, hex_map, pygame.Rect(0, 0, globals.VIEW_WIDTH, globals.VIEW_HEIGHT))
player = Player(background, map_view, globals.CAMERA_ROW, globals.CAMERA_COLUMN)

hex_map.fill_map()

background.fill(black)

while not done:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cell = map_view.screen_to_cell(pos)
            if cell:
                player.on_cell_click(cell)

    background.fill(black)

    map_view.draw()
    player.draw()

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
