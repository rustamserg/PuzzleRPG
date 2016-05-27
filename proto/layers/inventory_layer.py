import globals
from core.layer import Layer
from entities.button import Button
from data import tiles_data


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

    def post_draw(self, world, surface):
        player_layer = world.get_layer('PlayerLayer')
        player = player_layer.get_entity('player')

        col, row = 0, 0
        for item in player.inventory:
            px = globals.VIEW_OFFSET[0] + col * globals.INVENTORY_CELL_SIZE + globals.HEX_RADIUS/2
            py = globals.VIEW_OFFSET[1] + row * globals.INVENTORY_CELL_SIZE + globals.HEX_RADIUS/2
            surface.blit(world.tiles, (px, py), tiles_data.TILES[item.tile_name])
            col += 1
            if col == globals.INVENTORY_WIDTH:
                col = 0
                row += 1
                if row == globals.INVENTORY_HEIGHT:
                    row = 0

    def close_inventory(self, world):
        world.enable_layers()
        self.enable = False
