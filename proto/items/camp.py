from entities.item import Item


class Camp(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'camp', ['camp_01'])

    def on_action(self, world, by_entity):
        return True
