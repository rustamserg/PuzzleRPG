import globals
from ground import Ground, GroundType
from layer import Layer


class GroundLayer(Layer):
    def __init__(self, hex_map):
        Layer.__init__(self)
        self.hex_map = hex_map

    def fill_ground(self):
        for row in range(self.hex_map.height):
            for column in range(self.hex_map.width):
                cell = self.hex_map.get_cell(row, column)
                if cell:
                    if row < globals.CAMERA_ROW or row > globals.WORLD_WIDTH - globals.CAMERA_ROW:
                        self.entities.append(Ground(cell, GroundType.GRASS))
                    elif column < globals.CAMERA_COLUMN or column > globals.WORLD_HEIGHT - globals.CAMERA_COLUMN:
                        self.entities.append(Ground(cell, GroundType.GRASS))
                    else:
                        self.entities.append(Ground(cell, GroundType.WATER))
