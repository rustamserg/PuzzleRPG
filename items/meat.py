from entities.game_object import GameObject


class Meat(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'meat', ['meat_01'])

    def on_used(self, game, player):
        player.hunger = min(100, player.hunger + 10)
        return True
