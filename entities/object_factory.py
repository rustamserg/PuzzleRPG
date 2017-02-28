import importlib


class ObjectFactory:
    @staticmethod
    def create_item(item, ground_cell):
        parts = item.split('.')
        m = importlib.import_module('items.' + '.'.join(parts[:-1]))
        c = getattr(m, parts[-1])
        return c(ground_cell)

    @staticmethod
    def create_entity(item, ground_cell):
        parts = item.split('.')
        m = importlib.import_module('entities.' + '.'.join(parts[:-1]))
        c = getattr(m, parts[-1])
        return c(ground_cell)
