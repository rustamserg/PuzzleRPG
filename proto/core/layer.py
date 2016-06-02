class Layer:
    def __init__(self, enable=True):
        self.entities = []
        self.enable = enable

    def init(self, world):
        pass

    def start(self, world):
        pass

    @property
    def tag(self):
        return str(self.__class__.__name__)

    def add_entity(self, entity, tag=None):
        entity.tag = tag if tag else entity.tag
        self.entities.append(entity)

    def get_entity(self, tag):
        for entity in self.entities:
            if entity.tag == tag:
                return entity

    def del_entity(self, tag):
        for entity in self.entities:
            if entity.tag == tag:
                self.entities.remove(entity)
                return

    def on_click(self, world, pos, cell):
        if not self.enable:
            return

        for entity in self.entities:
            entity.on_pos_click(world, pos)
            if cell is not None:
                entity.on_cell_click(world, cell)

    def draw(self, world, surface):
        if not self.enable:
            return

        for entity in self.entities:
            entity.draw(world, surface)

    def update(self, world, turn):
        if not self.enable:
            return

        for entity in self.entities:
            entity.update(world, turn)
