from entities.game_object import GameObject


class Log(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'log', ['log_01'])

    def on_use(self, world, player):
        self.count -= 1
