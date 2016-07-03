class Layer:
    def __init__(self, z_order, enable=True):
        self.entities = []
        self.enable = enable
        self.z_order = z_order

    def init(self, game):
        pass

    def start(self, game):
        pass

    @property
    def tag(self):
        return str(self.__class__.__name__)

    def add_entity(self, entity, tag=None):
        entity.tag = tag if tag else entity.tag
        self.entities.append(entity)

    def get_entities(self, tag):
        return [ent for ent in self.entities if ent.tag == tag]

    def get_first_entity(self, tag):
        return next((ent for ent in self.entities if ent.tag == tag), None)

    def del_entity(self, tag):
        self.entities = [ent for ent in self.entities if ent.tag != tag]

    def on_click(self, game, pos, cell):
        if not self.enable:
            return

        for entity in self.entities:
            entity.on_pos_click(game, pos)
            if cell is not None:
                entity.on_cell_click(game, cell)

    def draw(self, game, surface):
        if not self.enable:
            return

        for entity in self.entities:
            entity.draw(game, surface)

    def update(self, game, turn):
        if not self.enable:
            return

        for entity in self.entities:
            entity.update(game, turn)
