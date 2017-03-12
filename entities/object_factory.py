import importlib


class ObjectFactory:
    @staticmethod
    def create_item(item, ground_cell):
        parts = item.split('.')
        m = importlib.import_module('items.' + '.'.join(parts[:-1]))
        c = getattr(m, parts[-1])
        return c(ground_cell)

    @staticmethod
    def create_script(script, ground_cell, **kwargs):
        parts = script.split('.')
        m = importlib.import_module('entities.' + '.'.join(parts[:-1]))
        c = getattr(m, parts[-1])
        return c(ground_cell, **kwargs)

    @staticmethod
    def create_ai(ai, ground_cell):
        parts = ai.split('.')
        m = importlib.import_module('ai.' + '.'.join(parts[:-1]))
        c = getattr(m, parts[-1])
        return c(ground_cell)
