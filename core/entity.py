class Entity:
    def __init__(self, tag=None):
        self.tag = tag if tag else str(self.__class__.__name__)

    def draw(self, game, surface):
        pass

    def on_pos_click(self, game, pos):
        pass

    def on_cell_click(self, game, cell):
        pass

    def update(self, game, turn):
        pass
