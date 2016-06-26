from entities.item import Item
from items.liana import Liana


class Stick(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'stick', ['stick_01'])

    def on_use(self, world, player):
        self.count -= 1

    def on_action(self, world, by_entity):
        items_layer = world.get_layer('ItemsLayer')

        if by_entity.archetype == 'sharp_stone':
            items_layer.del_entity(self.tag)
            new_tag = 'item_%i_%i' % (self.ground_cell.row, self.ground_cell.column)
            items_layer.add_entity(Liana(self.ground_cell), new_tag)
            return True
        return False

