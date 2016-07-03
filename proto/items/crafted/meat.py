from entities.game_object import GameObject


class Meat(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'meat', ['meat_01'])

    def on_used(self, game, player):
        player.hunger += 10
