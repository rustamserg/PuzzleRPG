import globals
from core.layer import Layer
from entities.editor_object import EditorObject


class EditorUILayer(Layer):
    def init(self, game):
        cell = game.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        cursor = EditorObject(cell)
        self.add_entity(cursor, 'cursor')
