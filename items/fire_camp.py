from entities.game_object import GameObject
from items.item_factory import ItemFactory


class FireCamp(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'fire_camp', ['fire_camp_01'])

    def try_pickup(self, game, by_entity):
        return False

    def try_combine(self, game, by_entity):
        if by_entity.archetype == 'raw_meat':
            inv_layer = game.scene.get_layer('InventoryLayer')
            inv_layer.add_to_inventory(ItemFactory.create('meat.Meat', None))
            return True
        return False

    def on_tod_changed(self, event):
        if event.hours == 6 and event.minutes == 0:
            items_layer = event.game.scene.get_layer('ItemsLayer')
            items_layer.del_entity(self.tag)
            items_layer.add_entity(ItemFactory.create('camp.Camp', self.ground_cell), self.tag)
