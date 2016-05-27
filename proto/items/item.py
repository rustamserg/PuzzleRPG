from core.entity import Entity
from data import tiles_data


class Item(Entity):
    def __init__(self, cell, tile_name):
        Entity.__init__(self)
        self.type = str(self.__class__.__name__)
        self.cell = cell
        self.tile_name = tile_name

    def draw(self, world, surface):
        if world.is_in_camera(self.cell):
            px, py = world.cell_to_ul_screen(self.cell)
            surface.blit(world.tiles, (px, py), tiles_data.TILES[self.tile_name])

    def on_action(self, world, by_entity):
        pass

    def on_use(self, world, by_entity):
        pass
