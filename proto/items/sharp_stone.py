from entities.item import Item


class SharpStone(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'sharp_stone', ['sharp_stone_01'])
