from core.cell import Cell
import globals
import json
from entities.ground import GroundType


class HexMap:
    def __init__(self, width, height, map_data=None):
        self.cells = []
        self.height = height
        self.width = width
        self.init_map()
        if map_data:
            self.load_map(map_data)

    def init_map(self):
        for row in range(self.height):
            self.cells.append([])
            for column in range(self.width):
                if row % 2 == 0 and column % 2 != 0:
                    self.cells[row].append(None)
                elif row % 2 != 0 and column % 2 == 0:
                    self.cells[row].append(None)
                else:
                    cell = Cell(row, column)
                    if row < globals.CAMERA_ROW or row > globals.WORLD_WIDTH - globals.CAMERA_ROW:
                        cell.ground = GroundType.WATER
                    elif column < globals.CAMERA_COLUMN or column > globals.WORLD_HEIGHT - globals.CAMERA_COLUMN:
                        cell.ground = GroundType.WATER
                    else:
                        cell.ground = GroundType.SAND
                    self.cells[row].append(cell)

    def load_map(self, map_name):
        with open(map_name, 'r') as data:
            map_data = json.load(data)
        for c in map_data['cells']:
            cell = self.get_cell(c['row'], c['column'])
            cell.ground = c['ground']
            cell.item = c['item']

    def save_map(self, map_name):
        map_data = {'cells': []}
        for row in range(self.height):
            for column in range(self.width):
                cell = self.get_cell(row, column)
                if cell:
                    cell_data = {'row': row, 'column': column, 'ground': cell.ground, 'item': cell.item}
                    map_data['cells'].append(cell_data)
        with open(map_name, 'w') as data:
            json.dump(map_data, data)

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
