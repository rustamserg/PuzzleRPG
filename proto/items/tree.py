from entities.item import Item
from items.log import Log


class Tree(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'tree', ['tree_01'])

    def on_action(self, world, by_entity):
        if by_entity.archetype == 'axe':
            items_layer = world.get_layer('ItemsLayer')
            items_layer.del_entity(self.tag)
            items_layer.add_entity(Log(self.ground_cell), self.tag)
        return True
