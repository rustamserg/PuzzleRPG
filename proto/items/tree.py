from entities.game_object import GameObject
from entities.game_object import ActionResult
from items.log import Log


class Tree(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'tree', ['tree_01'])

    def on_action(self, world, by_entity):
        if by_entity.archetype == 'axe':
            items_layer = world.get_layer('ItemsLayer')
            items_layer.del_entity(self.tag)
            items_layer.add_entity(Log(self.ground_cell), self.tag)
        return ActionResult.IGNORE
