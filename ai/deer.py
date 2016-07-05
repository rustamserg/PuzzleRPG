import random

from core.cell import Cell
from entities.game_object import GameObject
from items.raw_meat import RawMeat


class Deer(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'deer', ['deer_01'])

    def do_turn(self, game):
        ground_layer = game.scene.get_layer('GroundLayer')
        to_move = []
        for c in Cell.round_bbox(self.ground_cell):
            if ground_layer.can_move_to_cell(c):
                to_move.append(c)
        if len(to_move) > 0:
            self.ground_cell = random.choice(to_move)

    def try_pickup(self, game, by_entity):
        return False

    def try_combine(self, game, by_entity):
        if by_entity.archetype == 'spear':
            ai_layer = game.scene.get_layer('AILayer')
            items_layer = game.scene.get_layer('ItemsLayer')
            ai_layer.del_entity(self.tag)
            item_tag = 'item_%i_%i' % (self.ground_cell.row, self.ground_cell.column)
            items_layer.add_entity(RawMeat(self.ground_cell), item_tag)
        return False
