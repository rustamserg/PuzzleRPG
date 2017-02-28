from entities.game_object import GameObject


class ScriptObject(GameObject):
    def __init__(self, cell, editor_tile, **kwargs):
        GameObject.__init__(self, cell, 'script', [editor_tile])
        self.args = kwargs
