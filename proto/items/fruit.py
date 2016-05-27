from items.item import Item


class Fruit(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'fruit_01')

    def on_action(self, world, by_entity):
        if hasattr(by_entity, 'inventory'):
            items_layer = world.get_layer('ItemsLayer')
            items_layer.del_entity(self.tag)
            by_entity.inventory.append(self)

