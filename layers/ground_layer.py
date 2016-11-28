from core.layer import Layer
from entities.ground import Ground, GroundType


class GroundLayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)

    def init(self, game):
        for row in range(game.hex_map.height):
            for column in range(game.hex_map.width):
                cell = game.hex_map.get_cell(row, column)
                if cell:
                    self.add_entity(Ground(cell))

    def can_move_to_cell(self, cell):
        for ent in self.entities:
            if ent.cell == cell:
                if ent.cell.ground == GroundType.GRASS or ent.cell.ground == GroundType.SAND:
                    return True
        return False
