from items.item import Item
from items.test_item_03 import TestItem03


class TestItem02(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'test_item_02', 'test_item_02')

    def on_use(self, world, player):
        self.count -= 1

    def on_action(self, world, by_entity):
        items_layer = world.get_layer('ItemsLayer')

        if by_entity.archetype == 'test_item_01':
            items_layer.del_entity(self.tag)
            new_tag = 'item_%i_%i' % (self.ground_cell.row, self.ground_cell.column)
            items_layer.add_entity(TestItem03(self.ground_cell), new_tag)
