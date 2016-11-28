import globals
from core.layer import Layer
from entities.editor_object import EditorObject
from ui.button import Button
from entities.ground import GroundType
from ui.label import Label


class EditorUILayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)
        self.ground_type = GroundType.SAND

    def init(self, game):
        cell = game.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        cursor = EditorObject(cell)
        self.add_entity(cursor, 'cursor')

        btn = Button((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 100), 'Water', width=80)
        btn.on_click = self.on_water_ground
        self.add_entity(btn)

        btn = Button((globals.VIEW_OFFSET[0] + 100, globals.WINDOW_HEIGHT - 100), 'Grass', width=80)
        btn.on_click = self.on_grass_ground
        self.add_entity(btn)

        btn = Button((globals.VIEW_OFFSET[0] + 200, globals.WINDOW_HEIGHT - 100), 'Sand', width=80)
        btn.on_click = self.on_sand_ground
        self.add_entity(btn)

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
        self.get_first_entity('selected').text  = 'SAND'
