from entities.item import Item


class FireCamp(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'fire_camp', ['fire_camp_01'])

    def on_action(self, world, by_entity):
        return True
