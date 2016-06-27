import globals
from core.layer import Layer
from entities.game_object import ObjectLocation
from entities.player import Player
from items.empty_hand import EmptyHand


class PlayerLayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def init(self, world):
        spawn_cell = world.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        self.add_entity(Player(spawn_cell), 'player')
        self.take_item(world, EmptyHand(spawn_cell))

    def take_item(self, world, item):
        hand_item = self.get_first_entity('hand_item')
        if not hand_item:
            self.add_entity(item, 'hand_item')
            item.location = ObjectLocation.PLAYER
        else:
            if hand_item.archetype == item.archetype:
                hand_item.count += item.count
            else:
                self.del_entity('hand_item')
                self.add_entity(item, 'hand_item')
                item.location = ObjectLocation.PLAYER

                inv_layer = world.get_layer('InventoryLayer')
                inv_layer.add_to_inventory(hand_item)

    def use_item(self, world, item):
        if item.count > 0:
            player = self.get_first_entity('player')
            item.on_use(world, player)

    def pick_up_item(self, world, item):
        items_layer = world.get_layer('ItemsLayer')
        items_layer.del_entity(item.tag)

        hand_item = self.get_first_entity('hand_item')
        if hand_item and hand_item.archetype == item.archetype:
            hand_item.count += item.count
        else:
            inv_layer = world.get_layer('InventoryLayer')
            inv_layer.add_to_inventory(item)
