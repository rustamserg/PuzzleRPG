import random
from core.layer import Layer
from items.item import Item


class ItemsLayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def start(self, world):
        self.spawn(world)

    def spawn(self, world):
        ground_layer = world.get_layer('GroundLayer')
        to_spawn = 50
        while to_spawn > 0:
            row = random.randint(1, world.hex_map.height - 1)
            column = random.randint(1, world.hex_map.width - 1)
            cell = world.hex_map.get_cell(row, column)
            if cell is not None:
                if ground_layer.can_move_to_cell(cell):
                    self.add_entity(Item(cell, 'item_01'))
                    to_spawn -= 1
