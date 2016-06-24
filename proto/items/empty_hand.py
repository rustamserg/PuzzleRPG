from items.item import Item


class EmptyHand(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'empty_hand', ['empty_hand'])
        self.count = -1
