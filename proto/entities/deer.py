from core.cell import Cell
from core.entity import Entity
from data import tiles_data


class Deer(Entity):
    def __init__(self, cell, archetype):
        Entity.__init__(self)
        self.cell = cell
        self.archetype = archetype

    def draw(self, world, surface):
        if world.is_in_camera(self.cell):
            px, py = world.cell_to_ul_screen(self.cell)
            surface.blit(world.tiles, (px, py), tiles_data.TILES['deer'])

    def do_turn(self, world):
        ground_layer = world.get_layer('GroundLayer')
        for c in Cell.round_bbox(self.cell):
            if ground_layer.can_move_to_cell(c):
                self.cell = c
