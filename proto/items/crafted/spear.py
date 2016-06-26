from entities.item import Item


class Spear(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'spear', ['spear_01'])
