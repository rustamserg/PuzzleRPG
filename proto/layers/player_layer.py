import globals
from core.layer import Layer
from entities.player import Player


class PlayerLayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def init(self, world):
        spawn_cell = world.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        self.add_entity(Player(spawn_cell), 'player')
