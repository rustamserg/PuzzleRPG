import pygame
import globals
from core.layer import Layer
from entities.editor_object import EditorObject
from entities.ground import GroundType
from ui.icon import Icon

yellow = pygame.Color(255, 255, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


class EditorUILayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)
        self.ground_type = GroundType.SAND

    def init(self, game):
        cell = game.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        cursor = EditorObject(cell)
        self.add_entity(cursor)

        ico = Icon((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 100), tile_back=blue, data='water')
        ico.on_click = self.on_icon_selected
        self.add_entity(ico)

        ico = Icon((globals.VIEW_OFFSET[0] + 40, globals.WINDOW_HEIGHT - 100), tile_back=green, data='grass')
        ico.on_click = self.on_icon_selected
        self.add_entity(ico)

        ico = Icon((globals.VIEW_OFFSET[0] + 80, globals.WINDOW_HEIGHT - 100), tile_back=yellow, data='sand')
        ico.on_click = self.on_icon_selected
        self.add_entity(ico)

        ico = Icon((globals.VIEW_OFFSET[0] + 120, globals.WINDOW_HEIGHT - 100), 'sharp_stone_01', data='sharp_stone')
        ico.on_click = self.on_icon_selected
        self.add_entity(ico)

    def on_icon_selected(self, icon, game):
        if icon.data == 'water':
            self.ground_type = GroundType.WATER
        elif icon.data == 'grass':
            self.ground_type = GroundType.GRASS
        elif icon.data == 'sand':
            self.ground_type = GroundType.SAND
        for ent in self.get_entities('Icon'):
            ent.selected = False
        icon.selected = True
