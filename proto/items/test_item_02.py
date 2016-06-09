from items.item import Item


class TestItem02(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'test_item_02', 'test_item_02')

    def on_use(self, world, player):
        self.count -= 1

    def on_action(self, world, by_entity):
        player_layer = world.get_layer('PlayerLayer')

        if by_entity.archetype == 'test_item_01':
            player_layer.pick_up_item(world, self)
