import time

from globals import TurnType
from core.layer import Layer
from entities.object_factory import ObjectFactory


class AILayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)
        self.move_time = time.monotonic()

    def spawn_ai(self, archetype, tag, cell):
        if not self.get_ai_from_cell(cell):
            ai_entity = ObjectFactory.create_ai(archetype, cell)
            self.add_entity(ai_entity, tag)

    def get_ai_from_cell(self, cell):
        return next((ent for ent in self.entities if ent.ground_cell == cell), None)

    def update(self, game, turn):
        if turn == TurnType.PLAYER:
            self.move_time = time.monotonic()
            return

        diff_sec = time.monotonic() - self.move_time
        if diff_sec > 0.3:
            for ent in self.entities:
                ent.do_turn(game)
            game.end_turn()
