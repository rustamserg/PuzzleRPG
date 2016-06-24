import random
import globals
from core.layer import Layer
from core.cell import Cell
from items.sharp_stone import SharpStone
from items.stick import Stick


class ItemsLayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def start(self, world):
        self.spawn(world)

    def spawn(self, world):
        ground_layer = world.get_layer('GroundLayer')

        spawn_cell = world.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        spawn_cell = Cell.down_right(spawn_cell)
        self.add_entity(SharpStone(spawn_cell), 'item_%i_%i' % (spawn_cell.row, spawn_cell.column))

        to_spawn = 30
        while to_spawn > 0:
            row = random.randint(1, world.hex_map.height - 1)
            column = random.randint(1, world.hex_map.width - 1)
            cell = world.hex_map.get_cell(row, column)
            if cell is not None:
                if ground_layer.can_move_to_cell(cell):
                    if self.get_item_from_cell(cell) is None:
                        self.add_entity(Stick(cell), 'item_%i_%i' % (row, column))
                        to_spawn -= 1

    def get_item_from_cell(self, cell):
        for ent in self.entities:
            if ent.ground_cell == cell:
                return ent
        return None
