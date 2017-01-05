import globals
from globals import TurnType
from core.entity import Entity


class Player(Entity):
    def __init__(self, cell):
        Entity.__init__(self)
        self.cell = cell
        self.hunger = 0

    def draw(self, game, surface):
        if game.is_in_camera(self.cell):
            px, py = game.cell_to_ul_screen(self.cell)
            surface.blit(game.tiles.images['player'], (px, py))

    def on_tod_changed(self, event):
        self.hunger += globals.PLAYER_HUNGER_SPEED
        if self.hunger > 100:
            event.game.start()

    def on_cell_click(self, game, cell):
        if game.turn == TurnType.AI:
            return

        ground_layer = game.scene.get_layer('GroundLayer')
        items_layer = game.scene.get_layer('ItemsLayer')
        player_layer = game.scene.get_layer('PlayerLayer')
        ai_layer = game.scene.get_layer('AILayer')

        for c in game.hex_map.round_bbox(self.cell):
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
