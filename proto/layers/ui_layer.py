import globals
from core.layer import Layer
from entities.button import Button
from entities.label import Label


class UILayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def init(self, world):
        btn_inv = Button((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 100), 'Inventory')
        btn_inv.on_click = self.open_inventory
        self.add_entity(btn_inv)
        self.add_entity(Label((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 40), 'Status'), 'lbl_status')

    def update(self, world, turn):
        lbl = self.get_first_entity('lbl_status')
        lbl.text = 'Turn: %s' % turn

    @staticmethod
    def open_inventory(world):
        world.enable_layers(False)
        inv_layer = world.get_layer('InventoryLayer')
        inv_layer.enable = True
