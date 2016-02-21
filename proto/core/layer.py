class Layer:
    def __init__(self):
        self.entities = []

    @property
    def name(self):
        return str(self.__class__.__name__)

    def on_cell_click(self, map_view, cell):
        for entity in self.entities:
            entity.on_cell_click(map_view, cell)

    def draw(self, map_view, surface):
        for entity in self.entities:
            entity.draw(map_view, surface)
