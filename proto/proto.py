#!/usr/bin/env python
import pygame
from hex_map import HexMap
from map_view import MapView
from ground_layer import GroundLayer
from player_layer import PlayerLayer
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

ground_layer = GroundLayer(hex_map)
player_layer = PlayerLayer(hex_map)

ground_layer.fill_ground()
player_layer.spawn_player()

map_view.layers.append(ground_layer)
map_view.layers.append(player_layer)
# starting_cell = hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
# starting_cell.entities['camera'] = Camera(map_view)
# starting_cell.entities['player'] = Player()

while not done:

    clock.tick(60)
    background.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            map_view.on_click(pos)

    map_view.draw()

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
