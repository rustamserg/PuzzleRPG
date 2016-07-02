from globals import TurnType
from core.cell import Cell
from core.entity import Entity
from data import tiles_data


class Player(Entity):
    def __init__(self, cell):
        Entity.__init__(self)
        self.cell = cell
        self.health = 100
        self.hunger = 100
        self.fatigue = 100

    def draw(self, game, surface):
        if game.is_in_camera(self.cell):
            px, py = game.cell_to_ul_screen(self.cell)
            surface.blit(game.tiles, (px, py), tiles_data.TILES['player'])

    def on_tod_changed(self, event):
        self.hunger -= 5
        if self.hunger < 0:
            self.hunger = 0
            self.health -= 5

    def on_cell_click(self, game, cell):
        if game.turn == TurnType.AI:
            return

        ground_layer = game.main_scene.get_layer('GroundLayer')
        items_layer = game.main_scene.get_layer('ItemsLayer')
        player_layer = game.main_scene.get_layer('PlayerLayer')
        ai_layer = game.main_scene.get_layer('AILayer')

        for c in Cell.round_bbox(self.cell):
            if c == cell:
                item = items_layer.get_item_from_cell(cell)
                if item:
                    hand_item = player_layer.get_first_entity('hand_item')
                    if hand_item:
                        item.do_action(game, hand_item)
                    game.end_turn()
                    break
                else:
                    ai = ai_layer.get_ai_from_cell(cell)
                    if ai:
                        hand_item = player_layer.get_first_entity('hand_item')
                        if hand_item:
                            ai.do_action(game, hand_item)
                        game.end_turn()
                        break
                    else:
                        if ground_layer.can_move_to_cell(cell):
                            game.move_camera(cell)
                            self.cell = cell
                            game.end_turn()
                            break
