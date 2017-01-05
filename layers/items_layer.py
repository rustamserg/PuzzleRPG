from core.layer import Layer
from items.item_factory import ItemFactory


class ItemsLayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)

    def init(self, game):
        for row in range(game.hex_map.height):
            for column in range(game.hex_map.width):
                cell = game.hex_map.get_cell(row, column)
                if cell and cell.item:
                    self.spawn_item(cell)

    def spawn_item(self, cell):
        tag = 'item_%i_%i' % (cell.row, cell.column)
        self.del_entity(tag)
        if cell.item:
            item = ItemFactory.create(cell.item, cell)
            self.add_entity(item, tag)

    def get_item_from_cell(self, cell):
        for ent in self.entities:
            if ent.ground_cell == cell:
                return ent
        return None
