from entities.item import Item


class Meat(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'meat', ['meat_01'])

    def on_use(self, world, player):
        self.count -= 1
