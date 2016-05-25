class Entity:
    def __init__(self):
        self.tag = 'entity'

    def draw(self, world, surface):
        pass

    def on_pos_click(self, world, pos):
        pass

    def on_cell_click(self, world, cell):
        pass

    def update(self, world, turn):
        pass