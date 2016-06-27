import pygame
from core.entity import Entity
from data import tiles_data
import globals
import random


class ObjectLocation:
    def __init__(self):
        pass

    GROUND = 1
    INVENTORY = 2
    PLAYER = 3


class GameObject(Entity):
    def __init__(self, cell, archetype, tile_names):
        Entity.__init__(self)
        self.ground_cell = cell
        self.archetype = archetype
        self.inv_cell = None
        self.count = 1
        self.selected = False
        self.font = pygame.font.SysFont("monospace", 12)
        self.location = ObjectLocation.GROUND
        self.tile_name = random.choice(tile_names)

    def draw(self, world, surface):
        if self.location == ObjectLocation.GROUND:
            if world.is_in_camera(self.ground_cell):
                px, py = world.cell_to_ul_screen(self.ground_cell)
                surface.blit(world.tiles, (px, py), tiles_data.TILES[self.tile_name])

        elif self.location == ObjectLocation.INVENTORY:
            px = globals.VIEW_OFFSET[0] + self.inv_cell.column * globals.INVENTORY_CELL_SIZE + globals.HEX_RADIUS / 2
            py = globals.VIEW_OFFSET[1] + self.inv_cell.row * globals.INVENTORY_CELL_SIZE + globals.HEX_RADIUS / 2
            surface.blit(world.tiles, (px, py), tiles_data.TILES[self.tile_name])
            if self.count >= 0:
                label = self.font.render(str(self.count), 1, (255, 255, 0))
                surface.blit(label, (px + globals.HEX_RADIUS, py + globals.HEX_RADIUS))

        elif self.location == ObjectLocation.PLAYER:
            px, py = globals.WINDOW_WIDTH - 180, globals.WINDOW_HEIGHT - 100
            surface.blit(world.tiles, (px, py), tiles_data.TILES[self.tile_name])
            if self.count >= 0:
                label = self.font.render(str(self.count), 1, (255, 255, 0))
                surface.blit(label, (px + globals.HEX_RADIUS, py + globals.HEX_RADIUS))

    def on_pos_click(self, world, pos):
        if self.location == ObjectLocation.PLAYER:
            px, py = globals.WINDOW_WIDTH - 180, globals.WINDOW_HEIGHT - 100
            rect = pygame.Rect(px, py, globals.HEX_RADIUS, globals.HEX_RADIUS)

            if self.count > 0 and rect.collidepoint(pos):
                player_layer = world.get_layer('PlayerLayer')
                player_layer.use_item(world, self)
                self.count -= 1

    def do_action(self, world, by_entity):
        result = False
        if by_entity.count > 0:
            result = self.try_combine(world, by_entity)
            if result:
                by_entity.count -= 1
        if not result:
            result = self.try_pickup(world, by_entity)
            if result:
                player_layer = world.get_layer('PlayerLayer')
                player_layer.pick_up_item(world, self)

    def try_pickup(self, world, by_entity):
        return True

    def try_combine(self, world, by_entity):
        return False

    def on_use(self, world, player):
        pass
