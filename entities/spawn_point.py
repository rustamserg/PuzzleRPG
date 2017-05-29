from entities.script_object import ScriptObject
from globals import TurnType


class SpawnPoint(ScriptObject):
    def __init__(self, cell, **kwargs):
        ScriptObject.__init__(self, cell, **kwargs)
        self.counter = 0
        for key, value in kwargs.items():
            print("%s = %s" % (key, value))

    def update(self, game, turn):
        if turn == TurnType.AI:
            ai_layer = game.scene.get_layer('AILayer')
            tag_root = 'deer_%s' + str(self.ground_cell)
            spawned = ai_layer.get_entities(lambda ent: True if ent.tag.startswith(tag_root) else False)
            if len(spawned) < 4:
                self.counter = self.count + 1
                tag = "%s_%i" % (tag_root, self.counter)
                ai_layer.spawn_ai('deer.Deer', tag, self.ground_cell)
