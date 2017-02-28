from entities.script_object import ScriptObject


class SpawnPoint(ScriptObject):
    def __init__(self, cell, **kwargs):
        ScriptObject.__init__(self, cell, 'deer_01', **kwargs)
