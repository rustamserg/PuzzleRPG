import globals
from core.layer import Layer
from entities.ui.button import Button


class IntroLayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)

    def init(self, game):
        btn_inv = Button((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 100), 'Start')
        btn_inv.on_click = self.start_game
        self.add_entity(btn_inv)

    @staticmethod
    def start_game(game):
        game.director.activate_scene('GameScene', game)
