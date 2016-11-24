from core.cell import Cell
import globals
from entities.ground import GroundType


class HexMap:
    def __init__(self, width, height):
        self.cells = []
        self.height = height
        self.width = width
        self.init_map()
        self.load_map()

    def init_map(self):
        for row in range(self.height):
            self.cells.append([])
            for column in range(self.width):
                if row % 2 == 0 and column % 2 != 0:
                    self.cells[row].append(None)
                elif row % 2 != 0 and column % 2 == 0:
                    self.cells[row].append(None)
                else:
                    self.cells[row].append(Cell(row, column))

    def load_map(self):
        for row in range(self.height):
            for column in range(self.width):
                cell = self.get_cell(row, column)
                if cell:
                    if row < globals.CAMERA_ROW or row > globals.WORLD_WIDTH - globals.CAMERA_ROW:
                        cell.ground = GroundType.WATER
                    elif column < globals.CAMERA_COLUMN or column > globals.WORLD_HEIGHT - globals.CAMERA_COLUMN:
                        cell.ground = GroundType.WATER
                    else:
                        cell.ground = GroundType.SAND

    def get_cell(self, row, column):
        if 0 <= row < self.height:
            if 0 <= column < self.width:
                return self.cells[row][column]
        return None

    def round_bbox(self, cell):
        yield self.get_cell(cell.row - 2, cell.column)
        yield self.get_cell(cell.row - 1, cell.column + 1)
        yield self.get_cell(cell.row - 1, cell.column - 1)
        yield self.get_cell(cell.row + 2, cell.column)
        yield self.get_cell(cell.row + 1, cell.column + 1)
        yield self.get_cell(cell.row + 1, cell.column - 1)
