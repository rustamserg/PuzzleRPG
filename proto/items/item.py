import pygame
from core.entity import Entity
from data import tiles_data
import globals


class ItemLocation:
    def __init__(self):
        pass

    GROUND = 1
    INVENTORY = 2


class Item(Entity):
    def __init__(self, cell, tile_name):
        Entity.__init__(self)
        self.type = str(self.__class__.__name__)
        self.ground_cell = cell
        self.inv_cell = None
        self.count = 1
        self.font = pygame.font.SysFont("monospace", 12)
        self.location = ItemLocation.GROUND
        self.tile_name = tile_name

    def draw(self, world, surface):
        if self.location == ItemLocation.GROUND:
            if world.is_in_camera(self.ground_cell):
                px, py = world.cell_to_ul_screen(self.ground_cell)
                surface.blit(world.tiles, (px, py), tiles_data.TILES[self.tile_name])
        elif self.location == ItemLocation.INVENTORY:
            px = globals.VIEW_OFFSET[0] + self.inv_cell.column * globals.INVENTORY_CELL_SIZE
            py = globals.VIEW_OFFSET[1] + self.inv_cell.row * globals.INVENTORY_CELL_SIZE
            px += globals.HEX_RADIUS / 2
            py += globals.HEX_RADIUS / 2
            surface.blit(world.tiles, (px, py), tiles_data.TILES[self.tile_name])
            label = self.font.render(str(self.count), 1, (255, 255, 0))
            surface.blit(label, (px + globals.HEX_RADIUS, py + globals.HEX_RADIUS))

    def on_action(self, world, by_entity):
        pass

    def on_use(self, world, by_entity):
        pass
