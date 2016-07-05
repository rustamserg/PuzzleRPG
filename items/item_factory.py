import importlib


class ItemFactory:
    @staticmethod
    def create(item, ground_cell):
        parts = item.split('.')
        m = importlib.import_module('items.' + '.'.join(parts[:-1]))
        c = getattr(m, parts[-1])
        return c(ground_cell)
