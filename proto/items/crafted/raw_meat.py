from entities.item import Item


class RawMeat(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'raw_meat', ['raw_meat_01'])

    def on_use(self, world, player):
        self.count -= 1
