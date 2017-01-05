import pygame
import globals
from core.layer import Layer
from entities.editor_object import EditorObject
from entities.ground import GroundType
from ui.icon import Icon
from ui.button import Button

yellow = pygame.Color(255, 255, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


class EditorUILayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)
        self.ground_type = GroundType.SAND
        self.item = None
        self.icon_items = {'liana_01': 'liana.Liana',
                           'tree_01': 'tree.Tree',
                           'sharp_stone_01': 'sharp_stone.SharpStone',
                           'stick_01': 'stick.Stick',
                           'log_01': 'log.Log',
                           'raw_meat_01': 'raw_meat.RawMeat',
                           'camp_01': 'camp.Camp'}

    def init(self, game):
        cell = game.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        cursor = EditorObject(cell)
        self.add_entity(cursor)

        ico = Icon((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 100), tile='empty_hand', data='eraser')
        ico.on_click = self.on_icon_selected
        self.add_entity(ico)

        ico = Icon((globals.VIEW_OFFSET[0] + 40, globals.WINDOW_HEIGHT - 100), tile_back=blue, data='water')
        ico.on_click = self.on_icon_selected
        self.add_entity(ico)

        ico = Icon((globals.VIEW_OFFSET[0] + 80, globals.WINDOW_HEIGHT - 100), tile_back=green, data='grass')
        ico.on_click = self.on_icon_selected
        self.add_entity(ico)

        ico = Icon((globals.VIEW_OFFSET[0] + 120, globals.WINDOW_HEIGHT - 100), tile_back=yellow, data='sand')
        ico.on_click = self.on_icon_selected
        self.add_entity(ico)

        icon_x = globals.VIEW_OFFSET[0] + 120
        for item, item_class in self.icon_items.items():
            icon_x += 40
            ico = Icon((icon_x, globals.WINDOW_HEIGHT - 100), tile=item, data=item_class)
            ico.on_click = self.on_icon_selected
            self.add_entity(ico)

        btn = Button((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 50), 'Save')
        btn.on_click = self.on_save_map
        self.add_entity(btn)

        btn = Button((globals.VIEW_OFFSET[0] + 150, globals.WINDOW_HEIGHT - 50), 'Load')
        btn.on_click = self.on_load_map
        self.add_entity(btn)

    def on_icon_selected(self, icon, game):
        if icon.data == 'water':
            self.ground_type = GroundType.WATER
        elif icon.data == 'grass':
            self.ground_type = GroundType.GRASS
        elif icon.data == 'sand':
            self.ground_type = GroundType.SAND
        elif icon.data == 'eraser':
            self.item = None
        else:
            self.item = icon.data
        for ent in self.get_entities('Icon'):
            ent.selected = False
        icon.selected = True

    def on_save_map(self, game):
        game.hex_map.save_map('world.json')

    def on_load_map(self, game):
        game.hex_map.load_map('world.json')
        game.scene.get_layer('ItemsLayer').init(game)

