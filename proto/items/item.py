import pygame
from core.entity import Entity
from data import tiles_data
import globals
import random


class ItemLocation:
    def __init__(self):
        pass

    GROUND = 1
    INVENTORY = 2
    PLAYER = 3


class Item(Entity):
    def __init__(self, cell, archetype, tile_names):
        Entity.__init__(self)
        self.ground_cell = cell
        self.archetype = archetype
        self.inv_cell = None
        self.count = 1
        self.font = pygame.font.SysFont("monospace", 12)
        self.location = ItemLocation.GROUND
        self.tile_name = random.choice(tile_names)

    def draw(self, world, surface):
        if self.location == ItemLocation.GROUND:
            if world.is_in_camera(self.ground_cell):
                px, py = world.cell_to_ul_screen(self.ground_cell)
                surface.blit(world.tiles, (px, py), tiles_data.TILES[self.tile_name])

        elif self.location == ItemLocation.INVENTORY:
            px = globals.VIEW_OFFSET[0] + self.inv_cell.column * globals.INVENTORY_CELL_SIZE + globals.HEX_RADIUS / 2
            py = globals.VIEW_OFFSET[1] + self.inv_cell.row * globals.INVENTORY_CELL_SIZE + globals.HEX_RADIUS / 2
            surface.blit(world.tiles, (px, py), tiles_data.TILES[self.tile_name])
            if self.count > 0:
                label = self.font.render(str(self.count), 1, (255, 255, 0))
                surface.blit(label, (px + globals.HEX_RADIUS, py + globals.HEX_RADIUS))

        elif self.location == ItemLocation.PLAYER:
            px, py = globals.WINDOW_WIDTH - 180, globals.WINDOW_HEIGHT - 100
            surface.blit(world.tiles, (px, py), tiles_data.TILES[self.tile_name])
            if self.count > 0:
                label = self.font.render(str(self.count), 1, (255, 255, 0))
                surface.blit(label, (px + globals.HEX_RADIUS, py + globals.HEX_RADIUS))

    def on_pos_click(self, world, pos):
        if self.location == ItemLocation.INVENTORY:
            px = globals.VIEW_OFFSET[0] + self.inv_cell.column * globals.INVENTORY_CELL_SIZE + globals.HEX_RADIUS / 2
            py = globals.VIEW_OFFSET[1] + self.inv_cell.row * globals.INVENTORY_CELL_SIZE + globals.HEX_RADIUS / 2
            rect = pygame.Rect(px, py, globals.HEX_RADIUS, globals.HEX_RADIUS)

            if rect.collidepoint(pos):
                player_layer = world.get_layer('PlayerLayer')
                inv_layer = world.get_layer('InventoryLayer')
                inv_layer.del_from_inventory(self)
                player_layer.take_item(world, self)

        elif self.location == ItemLocation.PLAYER:
            px, py = globals.WINDOW_WIDTH - 180, globals.WINDOW_HEIGHT - 100
            rect = pygame.Rect(px, py, globals.HEX_RADIUS, globals.HEX_RADIUS)

            if rect.collidepoint(pos):
                player_layer = world.get_layer('PlayerLayer')
                player_layer.use_item(world, self)

    def on_action(self, world, by_entity):
        pass

    def on_use(self, world, player):
        pass
