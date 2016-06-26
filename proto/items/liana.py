from entities.item import Item


class Liana(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'liana', ['liana_01'])
