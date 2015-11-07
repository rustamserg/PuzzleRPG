#!/usr/bin/env python
import pygame
import random
from hex_map import HexMap
from map_view import MapView
from player import Player


# define some colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

colors = [blue, green]

pygame.init()

size = [500, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("HEX")

done = False
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background = background.convert()

WORLD_WIDTH = 100
WORLD_HEIGHT = 100
WORLD_VIEW_WIDTH = 12
WORLD_VIEW_HEIGHT = 20
WORLD_PLAYER_COLUMN = int(WORLD_VIEW_WIDTH/2)
WORLD_PLAYER_ROW = int(WORLD_VIEW_HEIGHT/2)

hex_map = HexMap(WORLD_WIDTH, WORLD_HEIGHT)
map_view = MapView(background, hex_map, pygame.Rect(0, 0, WORLD_VIEW_WIDTH, WORLD_VIEW_HEIGHT), (40, 40))
player = Player(background, map_view, WORLD_PLAYER_ROW, WORLD_PLAYER_COLUMN)

def fill_map():
    for row in range(hex_map.height):
        for column in range(hex_map.width):
            if hex_map.cells[row][column]:
                if row < WORLD_PLAYER_ROW or row > WORLD_WIDTH - WORLD_PLAYER_ROW:
                    hex_map.cells[row][column].content = colors[0]
                elif column < WORLD_PLAYER_COLUMN or column > WORLD_HEIGHT - WORLD_PLAYER_COLUMN:
                    hex_map.cells[row][column].content = colors[0]
                else:
                    hex_map.cells[row][column].content = colors[1]


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
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cell = map_view.screen_to_cell(pos)
            if cell:
                nr = pygame.Rect(0, 0, WORLD_VIEW_WIDTH, WORLD_VIEW_HEIGHT)
                nr = nr.move(cell.column - WORLD_PLAYER_COLUMN, cell.row - WORLD_PLAYER_ROW)
                if nr.top >= 0 and nr.left >= 0:
                    if WORLD_HEIGHT >= nr.top + WORLD_VIEW_HEIGHT:
                        if WORLD_WIDTH >= nr.left + WORLD_VIEW_WIDTH:
                            map_view.view = nr
                            player.column = cell.column
                            player.row = cell.row

    # fill empty cells
    background.fill(black)

    # draw the grid
    map_view.draw()
    player.draw()

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
