import pygame
from cell import Cell
from ground import Ground
import globals


green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

colors = [blue, green]


class HexMap:
    def __init__(self, width, height):
        self.cells = []
        self.radius = 25
        self.height = height
        self.width = width
        self.init_map()

    def init_map(self):
        for row in range(self.height):
            self.cells.append([])
            for column in range(self.width):
                if row % 2 == 0 and column % 2 != 0:
                    self.cells[row].append(None)
                elif row % 2 != 0 and column % 2 == 0:
                    self.cells[row].append(None)
                else:
                    self.cells[row].append(Cell(row, column, []))

    def get_cell(self, row, column):
        if 0 <= row < self.height:
            if 0 <= column < self.width:
                return self.cells[row][column]
        return None

    def fill_map(self):
        for row in range(self.height):
            for column in range(self.width):
                if self.cells[row][column]:
                    if row < globals.WORLD_PLAYER_ROW or row > globals.WORLD_WIDTH - globals.WORLD_PLAYER_ROW:
                        self.cells[row][column].content.append(Ground(self, colors[0]))
                    elif column < globals.WORLD_PLAYER_COLUMN or column > globals.WORLD_HEIGHT - globals.WORLD_PLAYER_COLUMN:
                        self.cells[row][column].content.append(Ground(self, colors[0]))
                    else:
                        self.cells[row][column].content.append(Ground(self, colors[1]))

