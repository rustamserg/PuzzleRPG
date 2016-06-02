from core.cell import Cell
from core.entity import Entity
from world import TurnType
from data import tiles_data


class Player(Entity):
    def __init__(self, cell):
        Entity.__init__(self)
        self.cell = cell

    def draw(self, world, surface):
        if world.is_in_camera(self.cell):
            px, py = world.cell_to_ul_screen(self.cell)
            surface.blit(world.tiles, (px, py), tiles_data.TILES['player'])

    def on_cell_click(self, world, cell):
        if world.turn == TurnType.AI:
            return

        ground_layer = world.get_layer('GroundLayer')
        items_layer = world.get_layer('ItemsLayer')
        player_layer = world.get_layer('PlayerLayer')

        for c in Cell.round_bbox(self.cell):
            if c == cell:
                item = items_layer.get_item_from_cell(cell)
                if item:
                    hand_item = player_layer.get_entity('hand_item')
                    by_entity = hand_item if hand_item else self
                    item.on_action(world, by_entity)
                    world.end_turn()
                    break
                else:
                    if ground_layer.can_move_to_cell(cell):
                        world.move_camera(cell)
                        self.cell = cell
                        world.end_turn()
                        break
