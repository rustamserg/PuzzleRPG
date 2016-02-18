class Entity:
    def __init__(self, cell):
        self.owner = cell

    @property
    def entity_type(self):
        return str(self.__class__.__name__)

    def draw(self, surface):
        pass

    def on_cell_click(self, cell):
        pass
