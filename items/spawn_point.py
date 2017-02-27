from entities.game_object import GameObject


class SpawnPoint(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'script', ['spawn_marker'])
