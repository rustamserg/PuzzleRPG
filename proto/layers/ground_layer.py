import globals
from core.layer import Layer
from entities.ground import Ground, GroundType


class GroundLayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def init(self, world):
        for row in range(world.hex_map.height):
            for column in range(world.hex_map.width):
                cell = world.hex_map.get_cell(row, column)
                if cell:
                    if row < globals.CAMERA_ROW or row > globals.WORLD_WIDTH - globals.CAMERA_ROW:
                        self.add_entity(Ground(cell, GroundType.WATER))
                    elif column < globals.CAMERA_COLUMN or column > globals.WORLD_HEIGHT - globals.CAMERA_COLUMN:
                        self.add_entity(Ground(cell, GroundType.WATER))
                    else:
                        self.add_entity(Ground(cell, GroundType.GRASS))

    def can_move_to_cell(self, cell):
        for ent in self.entities:
            if ent.cell == cell and ent.ground_type == GroundType.GRASS:
                return True
        return False
