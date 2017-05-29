from entities.game_object import GameObject


class ScriptObject(GameObject):
    def __init__(self, cell, **kwargs):
        GameObject.__init__(self, cell, 'script')
        self.args = kwargs
