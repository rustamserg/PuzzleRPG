from core.entity import Entity
from items.spear import Spear


class Craft(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.recipes = {Spear(None): ['sharp_stone', 'stick', 'liana']}

    def combine(self, items):
        for crafted, recipe in self.recipes.items():
            test = list(recipe)
            for item in items:
                if item.archetype in test:
                    test.remove(item.archetype)
            if len(test) == 0:
                return crafted
        return None
