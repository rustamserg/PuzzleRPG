from entities.game_object import GameObject


class Spear(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'spear', ['spear_01'])
