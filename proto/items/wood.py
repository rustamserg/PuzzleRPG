from items.item import Item


class Wood(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'wood', 'wood_01')

    def on_action(self, world, by_entity):
        if by_entity.tag == 'player':
            items_layer = world.get_layer('ItemsLayer')
            inv_layer = world.get_layer('InventoryLayer')

            items_layer.del_entity(self.tag)
            inv_layer.add_to_inventory(self)

    def on_use(self, world, player):
        self.count -= 1
