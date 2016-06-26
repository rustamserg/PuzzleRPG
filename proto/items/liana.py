from entities.game_object import GameObject


class Liana(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'liana', ['liana_01'])
