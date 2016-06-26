from entities.item import Item


class Stick(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'stick', ['stick_01'])

