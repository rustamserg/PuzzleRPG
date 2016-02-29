import globals
from core.layer import Layer
from entities.ground import Ground, GroundType


class GroundLayer(Layer):
    def __init__(self, hex_map):
        Layer.__init__(self)
        self.hex_map = hex_map

    def init(self):
        for row in range(self.hex_map.height):
            for column in range(self.hex_map.width):
                cell = self.hex_map.get_cell(row, column)
                if cell:
                    if row < globals.CAMERA_ROW or row > globals.WORLD_WIDTH - globals.CAMERA_ROW:
                        self.add_entity(Ground(cell, GroundType.WATER))
                    elif column < globals.CAMERA_COLUMN or column > globals.WORLD_HEIGHT - globals.CAMERA_COLUMN:
                        self.add_entity(Ground(cell, GroundType.WATER))
                    else:
                        self.add_entity(Ground(cell, GroundType.GRASS))
