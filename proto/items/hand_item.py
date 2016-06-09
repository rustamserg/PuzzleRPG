from items.item import Item


class HandItem(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'hand', 'hand_item')
        self.count = -1
