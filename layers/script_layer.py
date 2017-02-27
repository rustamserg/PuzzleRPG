from core.layer import Layer
from items.item_factory import ItemFactory


class ScriptLayer(Layer):
    def __init__(self, z_order):
        Layer.__init__(self, z_order)

    def init(self, game):
        for row in range(game.hex_map.height):
            for column in range(game.hex_map.width):
                cell = game.hex_map.get_cell(row, column)
                if cell and cell.script:
                    self.spawn_script(cell)

    def spawn_script(self, cell):
        tag = 'script_%i_%i' % (cell.row, cell.column)
        self.del_entity(tag)
        if cell.script:
            script = ItemFactory.create(cell.script, cell)
            self.add_entity(script, tag)

    def draw(self, game, surface):
        if game.is_editor:
            Layer.draw(self, game, surface)

    def on_click(self, game, pos, cell):
        pass
