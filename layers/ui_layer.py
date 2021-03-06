import globals
from core.layer import Layer
from ui.button import Button
from ui.label import Label


class UILayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)

    def init(self, game):
        btn_inv = Button((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 100), 'Inventory')
        btn_inv.on_click = self.open_inventory

        self.add_entity(btn_inv)
        self.add_entity(Label((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 40), 'Status'), 'lbl_status')
        self.add_entity(Label((globals.VIEW_OFFSET[0] + 150, 10)), 'lbl_hunger')
        self.add_entity(Label((globals.WINDOW_WIDTH - 200, 10)), 'lbl_tod')

    def update(self, game, turn):
        lbl = self.get_first_entity_by_tag('lbl_status')
        lbl.text = 'Turn: %s' % turn

        player_layer = game.scene.get_layer('PlayerLayer')
        lbl = self.get_first_entity_by_tag('lbl_hunger')
        lbl.text = 'Hunger: %i' % player_layer.get_hunger()

        lbl = self.get_first_entity_by_tag('lbl_tod')
        lbl.text = 'Time: %.2i:%.2i' % (game.tod[0], game.tod[1])

    @staticmethod
    def open_inventory(game):
        game.scene.enable_layers(False)
        inv_layer = game.scene.get_layer('InventoryLayer')
        inv_layer.enable = True
