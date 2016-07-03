from entities.game_object import GameObject


class SharpStone(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'sharp_stone', ['sharp_stone_01'])
