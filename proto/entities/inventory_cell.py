import globals
from entities.button import Button


class InventoryCell(Button):
    def __init__(self, pos):
        Button.__init__(self, pos, '', globals.INVENTORY_CELL_SIZE, globals.INVENTORY_CELL_SIZE)
        self.item = None
