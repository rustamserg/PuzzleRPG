import globals
from core.layer import Layer
from entities.button import Button


class InventoryLayer(Layer):
    def __init__(self):
        Layer.__init__(self, False)

    def init(self, world):
        for row in range(globals.INVENTORY_HEIGHT):
            for col in range(globals.INVENTORY_WIDTH):
                pos_x = globals.VIEW_OFFSET[0] + col * globals.INVENTORY_CELL_SIZE
                pos_y = globals.VIEW_OFFSET[1] + row * globals.INVENTORY_CELL_SIZE
                cell = Button((pos_x, pos_y), '', globals.INVENTORY_CELL_SIZE, globals.INVENTORY_CELL_SIZE)
                self.add_entity(cell)

        btn_inv = Button((globals.WINDOW_WIDTH - 180, globals.WINDOW_HEIGHT - 100), 'Back')
        btn_inv.on_click = self.close_inventory
        self.add_entity(btn_inv)

    def close_inventory(self, world):
        world.enable_layers()
        self.enable = False

