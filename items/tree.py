from entities.game_object import GameObject
from entities.object_factory import ObjectFactory


class Tree(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'tree', ['tree_01', 'tree_02'])

    def try_pickup(self, game, by_entity):
        return False

    def try_combine(self, game, by_entity):
        if by_entity.archetype == 'axe':
            items_layer = game.scene.get_layer('ItemsLayer')
            items_layer.del_entity(self.tag)
            items_layer.add_entity(ObjectFactory.create_item('log.Log', self.ground_cell), self.tag)
        return False
