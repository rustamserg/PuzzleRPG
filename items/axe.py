from entities.game_object import GameObject


class Axe(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'axe', ['axe_01'])
