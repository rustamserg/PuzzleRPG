from entities.script_object import ScriptObject
from entities.object_factory import ObjectFactory
from globals import TurnType


class SpawnPoint(ScriptObject):
    def __init__(self, cell, **kwargs):
        ScriptObject.__init__(self, cell, **kwargs)
        self.counter = 0
        self.ai_count = 0
        self.ai_type = None
        for key, value in kwargs.items():
            setattr(self, key, value)
        ai_entity = ObjectFactory.create_ai(self.ai_type, cell)
        self.tile_name = ai_entity.tile_name

    def update(self, game, turn):
        if turn == TurnType.AI:
            ai_layer = game.scene.get_layer('AILayer')
            tag_root = 'ai_%s' + str(self.ground_cell)
            spawned = ai_layer.get_entities(lambda ent: True if ent.tag.startswith(tag_root) else False)
            if len(spawned) < self.ai_count:
                self.counter = self.counter + 1
                tag = "%s_%i" % (tag_root, self.counter)
                ai_layer.spawn_ai(self.ai_type, tag, self.ground_cell)
