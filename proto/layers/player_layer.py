import globals
from core.layer import Layer
from entities.player import Player


class PlayerLayer(Layer):
    def __init__(self, hex_map):
        Layer.__init__(self)
        self.hex_map = hex_map

    def spawn_player(self):
        spawn_cell = self.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        self.entities.append(Player(spawn_cell))