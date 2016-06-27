import random
import time

from ai.deer import Deer
from core.layer import Layer
from world import TurnType


class AILayer(Layer):
    def __init__(self):
        Layer.__init__(self)
        self.move_time = time.monotonic()

    def start(self, world):
        ground_layer = world.get_layer('GroundLayer')
        to_spawn = 10
        while to_spawn > 0:
            row = random.randint(1, world.hex_map.height/4 - 1)
            column = random.randint(1, world.hex_map.width/4 - 1)
            cell = world.hex_map.get_cell(row, column)
            if cell is not None:
                if ground_layer.can_move_to_cell(cell):
                    self.add_entity(Deer(cell), 'deer_%i' % to_spawn)
                    to_spawn -= 1

    def get_ai_from_cell(self, cell):
        for ent in self.entities:
            if ent.ground_cell == cell:
                return ent
        return None

    def update(self, world, turn):
        if turn == TurnType.PLAYER:
            self.move_time = time.monotonic()
            return

        diff_sec = time.monotonic() - self.move_time
        if diff_sec > 0.3:
            for ent in self.entities:
                ent.do_turn(world)
            world.end_turn()

