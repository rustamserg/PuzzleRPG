import random
from core.layer import Layer
from items.item_factory import ItemFactory


class ItemsLayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)

    def start(self, game):
        ground_layer = game.scene.get_layer('GroundLayer')

        to_spawn = 30
        while to_spawn > 0:
            row = random.randint(1, game.hex_map.height / 4 - 1)
            column = random.randint(1, game.hex_map.width / 4 - 1)
            cell = game.hex_map.get_cell(row, column)
            if cell is not None:
                if ground_layer.can_move_to_cell(cell):
                    if self.get_item_from_cell(cell) is None:
                        self.spawn_item(cell, 'item_%i_%i' % (row, column))
                        to_spawn -= 1

    def get_item_from_cell(self, cell):
        for ent in self.entities:
            if ent.ground_cell == cell:
                return ent
        return None

    def spawn_item(self, cell, tag):
        items = ['sharp_stone.SharpStone', 'stick.Stick', 'liana.Liana', 'tree.Tree', 'camp.Camp', 'log.Log']
        item = ItemFactory.create(random.choice(items), cell)
        self.add_entity(item, tag)
