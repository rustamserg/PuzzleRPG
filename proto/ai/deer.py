from core.cell import Cell
from entities.game_object import ActionResult
from entities.game_object import GameObject
from items.crafted.raw_meat import RawMeat


class Deer(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'deer', ['deer_01'])

    def do_turn(self, world):
        ground_layer = world.get_layer('GroundLayer')
        for c in Cell.round_bbox(self.ground_cell):
            if ground_layer.can_move_to_cell(c):
                self.ground_cell = c

    def do_action(self, world, by_entity):
        if by_entity.archetype == 'spear':
            items_layer = world.get_layer('ItemsLayer')
            items_layer.del_entity(self.tag)
            items_layer.add_entity(RawMeat(self.ground_cell), self.tag)
        return ActionResult.IGNORE
