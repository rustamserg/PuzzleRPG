from entities.item import Item


class Log(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'log', ['log_01'])

    def on_use(self, world, player):
        self.count -= 1
