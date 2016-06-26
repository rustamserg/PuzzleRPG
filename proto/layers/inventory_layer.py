import globals
from core.cell import Cell
from core.layer import Layer
from entities.button import Button
from entities.craft import Craft
from entities.inventory_cell import InventoryCell
from entities.game_object import ObjectLocation


class InventoryLayer(Layer):
    def __init__(self):
        Layer.__init__(self, False)

    def init(self, world):
        self.add_entity(Craft(), 'craft')

        for row in range(globals.INVENTORY_HEIGHT):
            for col in range(globals.INVENTORY_WIDTH):
                pos_x = globals.VIEW_OFFSET[0] + col * globals.INVENTORY_CELL_SIZE
                pos_y = globals.VIEW_OFFSET[1] + row * globals.INVENTORY_CELL_SIZE
                cell = InventoryCell((pos_x, pos_y))
                self.add_entity(cell, 'cell_%i_%i' % (row, col))

        btn_inv = Button((globals.WINDOW_WIDTH - 180, globals.WINDOW_HEIGHT - 100), 'Back')
        btn_inv.on_click = self.close_inventory
        self.add_entity(btn_inv)

        btn_craft = Button((globals.WINDOW_WIDTH - 380, globals.WINDOW_HEIGHT - 100), 'Craft')
        btn_craft.on_click = self.do_craft
        self.add_entity(btn_craft)

    def del_from_inventory(self, item):
        inv_cell = self.get_first_entity('cell_%i_%i' % (item.inv_cell.row, item.inv_cell.column))
        inv_cell.item = None
        self.del_entity(item.tag)

    def add_to_inventory(self, item):
        for row in range(globals.INVENTORY_HEIGHT):
            for col in range(globals.INVENTORY_WIDTH):
                inv_cell = self.get_first_entity('cell_%i_%i' % (row, col))
                if inv_cell.item and inv_cell.item.archetype == item.archetype:
                    inv_cell.item.count += 1
                    return

        for row in range(globals.INVENTORY_HEIGHT):
            for col in range(globals.INVENTORY_WIDTH):
                inv_cell = self.get_first_entity('cell_%i_%i' % (row, col))
                if not inv_cell.item:
                    inv_cell.item = item
                    item.location = ObjectLocation.INVENTORY
                    item.inv_cell = Cell(row, col)
                    item.tag = 'item_%i_%i' % (row, col)
                    self.add_entity(item, item.tag)
                    return

    def get_selected_cells(self):
        selected = []
        for row in range(globals.INVENTORY_HEIGHT):
            for col in range(globals.INVENTORY_WIDTH):
                cell = self.get_first_entity('cell_%i_%i' % (row, col))
                if cell.selected:
                    selected.append(cell.item)
        return selected

    def reset_selection(self):
        for row in range(globals.INVENTORY_HEIGHT):
            for col in range(globals.INVENTORY_WIDTH):
                cell = self.get_first_entity('cell_%i_%i' % (row, col))
                cell.selected = False

    def close_inventory(self, world):
        selected = self.get_selected_cells()
        if len(selected) == 1:
            item = selected[0]
            self.del_from_inventory(item)
            player_layer = world.get_layer('PlayerLayer')
            player_layer.take_item(world, item)
        self.reset_selection()
        world.enable_layers()
        self.enable = False

    def do_craft(self, world):
        selected = self.get_selected_cells()
        if len(selected) > 1:
            craft = self.get_first_entity('craft')
            if craft:
                crafted = craft.combine(selected)
                if crafted:
                    for item in selected:
                        item.count -= 1
                        if item.count == 0:
                            self.del_from_inventory(item)
                    self.add_to_inventory(crafted)
        self.reset_selection()
