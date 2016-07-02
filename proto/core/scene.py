class Scene:
    def __init__(self):
        self.layers = {}
        self.sorted_layers = []

    @property
    def tag(self):
        return str(self.__class__.__name__)

    def add_layer(self, layer):
        self.layers[layer.tag] = layer
        self.sorted_layers = [x for tag, x in sorted(self.layers.items(), key=lambda x: x[1].z_order)]

    def get_layer(self, tag):
        return self.layers[tag]

    def enable_layers(self, enable=True):
        for layer in self.sorted_layers:
            layer.enable = enable

    def compose(self, game):
        pass

    def init(self, game):
        for layer in self.sorted_layers:
            layer.init(game)

    def start(self, game):
        for layer in self.sorted_layers:
            layer.start(game)

    def on_click(self, game, pos, cell):
        for layer in self.sorted_layers:
            layer.on_click(game, pos, cell)

    def draw(self, game, surface):
        for layer in self.sorted_layers:
            layer.draw(game, surface)

    def update(self, game, turn_type):
        for layer in self.sorted_layers:
            layer.update(game, turn_type)
