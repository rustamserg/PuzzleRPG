from entities.game_object import GameObject
from items.item_factory import ItemFactory


class Camp(GameObject):
    def __init__(self, cell):
        GameObject.__init__(self, cell, 'camp', ['camp_01'])

    def try_pickup(self, game, by_entity):
        return False

    def try_combine(self, game, by_entity):
        if by_entity.archetype == 'log':
            fire_camp = ItemFactory.create('fire_camp.FireCamp', self.ground_cell)
            game.subscribe(fire_camp.on_tod_changed)
            items_layer = game.scene.get_layer('ItemsLayer')
            items_layer.del_entity(self.tag)
            items_layer.add_entity(fire_camp, self.tag)
            return True
        return False
