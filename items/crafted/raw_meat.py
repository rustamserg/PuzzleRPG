from entities.game_object import GameObject


class RawMeat(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'raw_meat', ['raw_meat_01'])

