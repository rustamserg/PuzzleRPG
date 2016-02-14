from cell import Cell
from ground import Ground, GroundType
import globals


class HexMap:
    def __init__(self, width, height):
        self.cells = []
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
                    self.cells[row].append(Cell(row, column, {}))

    def get_cell(self, row, column):
        if 0 <= row < self.height:
            if 0 <= column < self.width:
                return self.cells[row][column]
        return None

    def fill_ground(self):
        for row in range(self.height):
            for column in range(self.width):
                if self.cells[row][column]:
                    if row < globals.CAMERA_ROW or row > globals.WORLD_WIDTH - globals.CAMERA_ROW:
                        self.cells[row][column].entities['ground'] = Ground(GroundType.GRASS)
                    elif column < globals.CAMERA_COLUMN or column > globals.WORLD_HEIGHT - globals.CAMERA_COLUMN:
                        self.cells[row][column].entities['ground'] = Ground(GroundType.GRASS)
                    else:
                        self.cells[row][column].entities['ground'] = Ground(GroundType.WATER)
