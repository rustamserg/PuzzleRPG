#!/usr/bin/env python
import pygame
import random
from hex_map import HexMap
from map_view import MapView

# define some colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

colors = [green, blue]

pygame.init()

size = [350, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("HEX")

done = False
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background = background.convert()

hex_map = HexMap(300, 300)
map_view = MapView(background, hex_map, pygame.Rect(0, 0, 8, 20), pygame.Rect(40, 40, 0, 0))


def fill_map():
    for row in range(hex_map.height):
        for column in range(hex_map.width):
            if hex_map.cells[row][column]:
                hex_map.cells[row][column].content = colors[random.randint(1, len(colors)) - 1]


# init empty map
fill_map()
background.fill(black)

# main loop
while not done:

    # limit to 60 frames per second
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                map_view.view = map_view.view.move(0, -2)
            if event.key == pygame.K_DOWN:
                map_view.view = map_view.view.move(0, 2)

    # fill empty cells
    background.fill(black)

    # draw the grid
    map_view.draw()

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
