import copy

from core.entity import Entity
from items.crafted.spear import Spear
from items.crafted.axe import Axe


class Craft(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.recipes = {Spear(None): ['sharp_stone', 'stick', 'liana'],
                        Axe(None): ['sharp_stone', 'log', 'liana']}

    def combine(self, items):
        for crafted, recipe in self.recipes.items():
            test = list(recipe)
            if len(test) == len(items):
                for item in items:
                    if item.archetype in test:
                        test.remove(item.archetype)
                if len(test) == 0:
                    return copy.copy(crafted)
        return None
