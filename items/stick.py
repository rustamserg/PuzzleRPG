from entities.game_object import GameObject


class Stick(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'stick', ['stick_01'])

