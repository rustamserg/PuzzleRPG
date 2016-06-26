from entities.item import Item


class Axe(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'axe', ['axe_01'])
