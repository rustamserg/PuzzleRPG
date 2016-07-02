from entities.game_object import GameObject
from items.crafted.meat import Meat


class FireCamp(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'fire_camp', ['fire_camp_01'])

    def try_pickup(self, game, by_entity):
        return False

    def try_combine(self, game, by_entity):
        if by_entity.archetype == 'raw_meat':
            inv_layer = game.main_scene.get_layer('InventoryLayer')
            inv_layer.add_to_inventory(Meat(None))
            return True
        return False
