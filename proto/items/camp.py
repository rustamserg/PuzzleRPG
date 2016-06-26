from entities.item import Item
from entities.item import ActionResult
from items.crafted.fire_camp import FireCamp


class Camp(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'camp', ['camp_01'])

    def on_action(self, world, by_entity):
        if by_entity.archetype == 'log':
            items_layer = world.get_layer('ItemsLayer')
            items_layer.del_entity(self.tag)
            items_layer.add_entity(FireCamp(self.ground_cell), self.tag)
            return ActionResult.USED

        return ActionResult.IGNORE
