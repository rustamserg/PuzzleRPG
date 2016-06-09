from items.item import Item


class TestItem03(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'test_item_03', 'test_item_03')

    def on_use(self, world, player):
        self.count -= 1
