import globals
from core.layer import Layer
from entities.editor_object import EditorObject
from ui.button import Button
from entities.ground import GroundType
from ui.label import Label
from ui.icon import Icon


class EditorUILayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)
        self.ground_type = GroundType.SAND

    def init(self, game):
        cell = game.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        cursor = EditorObject(cell)
        self.add_entity(cursor, 'cursor')

        btn = Button((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 100), 'Water', width=70)
        btn.on_click = self.on_water_ground
        self.add_entity(btn)

        btn = Button((globals.VIEW_OFFSET[0] + 75, globals.WINDOW_HEIGHT - 100), 'Grass', width=70)
        btn.on_click = self.on_grass_ground
        self.add_entity(btn)

        btn = Button((globals.VIEW_OFFSET[0] + 150, globals.WINDOW_HEIGHT - 100), 'Sand', width=70)
        btn.on_click = self.on_sand_ground
        self.add_entity(btn)

        ico = Icon((globals.VIEW_OFFSET[0] + 300, globals.WINDOW_HEIGHT - 100), 'sharp_stone_01')
        ico.on_click = self.on_sharp_stone_item
        self.add_entity(ico)

        lbl = Label((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 30), 'SAND')
        self.add_entity(lbl, 'selected')

    def on_water_ground(self, game):
        self.ground_type = GroundType.WATER
        self.get_first_entity('selected').text = 'WATER'

    def on_grass_ground(self, game):
        self.ground_type = GroundType.GRASS
        self.get_first_entity('selected').text = 'GRASS'

    def on_sand_ground(self, game):
        self.ground_type = GroundType.SAND
        self.get_first_entity('selected').text = 'SAND'

    def on_sharp_stone_item(self, game):
        self.get_first_entity('selected').text = 'Stone'
