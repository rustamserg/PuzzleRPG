import globals
from core.layer import Layer
from entities.player import Player
from items.item import ItemLocation


class PlayerLayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def init(self, world):
        spawn_cell = world.hex_map.get_cell(globals.CAMERA_ROW, globals.CAMERA_COLUMN)
        self.add_entity(Player(spawn_cell), 'player')

    def take_to_hand(self, world, item):
        hand_item = self.get_first_entity('hand_item')
        if not hand_item:
            self.add_entity(item, 'hand_item')
            item.location = ItemLocation.PLAYER
        else:
            if hand_item.archetype == item.archetype:
                hand_item.count += item.count
            else:
                self.del_entity('hand_item')
                self.add_entity(item, 'hand_item')
                item.location = ItemLocation.PLAYER

                inv_layer = world.get_layer('InventoryLayer')
                inv_layer.add_to_inventory(hand_item)

    def use_item(self, world, item):
        player = self.get_first_entity('player')
        item.on_use(world, player)
        if item.count == 0:
            self.del_entity('hand_item')
