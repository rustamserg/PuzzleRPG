import globals
from core.layer import Layer
from core.cell import Cell
from entities.inventory_cell import InventoryCell
from entities.button import Button
from items.item import ItemLocation


class InventoryLayer(Layer):
    def __init__(self):
        Layer.__init__(self, False)

    def init(self, world):
        for row in range(globals.INVENTORY_HEIGHT):
            for col in range(globals.INVENTORY_WIDTH):
                pos_x = globals.VIEW_OFFSET[0] + col * globals.INVENTORY_CELL_SIZE
                pos_y = globals.VIEW_OFFSET[1] + row * globals.INVENTORY_CELL_SIZE
                cell = InventoryCell((pos_x, pos_y))
                self.add_entity(cell, 'cell_%i_%i' % (row, col))

        btn_inv = Button((globals.WINDOW_WIDTH - 180, globals.WINDOW_HEIGHT - 100), 'Back')
        btn_inv.on_click = self.close_inventory
        self.add_entity(btn_inv)

    def add_to_inventory(self, item):
        for row in range(globals.INVENTORY_HEIGHT):
            for col in range(globals.INVENTORY_WIDTH):
                inv_cell = self.get_entity('cell_%i_%i' % (row, col))
                if inv_cell.item and inv_cell.item.type == item.type:
                    inv_cell.item.count += 1
                    return

        for row in range(globals.INVENTORY_HEIGHT):
            for col in range(globals.INVENTORY_WIDTH):
                inv_cell = self.get_entity('cell_%i_%i' % (row, col))
                if not inv_cell.item:
                    inv_cell.item = item
                    item.location = ItemLocation.INVENTORY
                    item.inv_cell = Cell(row, col)
                    self.add_entity(item, item.tag)
                    return

    def close_inventory(self, world):
        world.enable_layers()
        self.enable = False
