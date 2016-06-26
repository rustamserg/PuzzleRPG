from entities.item import Item
from entities.item import ActionResult
from items.crafted.meat import Meat


class FireCamp(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'fire_camp', ['fire_camp_01'])

    def on_action(self, world, by_entity):
        if by_entity.archetype == 'raw_meat':
            inv_layer = world.get_layer('InventoryLayer')
            inv_layer.add_to_inventory(Meat(None))
            return ActionResult.USED

        return ActionResult.IGNORE
