from entities.game_object import GameObject


class EmptyHand(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'empty_hand', ['empty_hand'])
        self.count = -1
