class Layer:
    def __init__(self, z_order, enable=True):
        self.entities = []
        self.enable = enable
        self.z_order = z_order
        self.world = None

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

    def get_entities(self, tag):
        return [ent for ent in self.entities if ent.tag == tag]

    def get_first_entity(self, tag):
        return next((ent for ent in self.entities if ent.tag == tag), None)

    def del_entity(self, tag):
        self.entities = [ent for ent in self.entities if ent.tag != tag]

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
