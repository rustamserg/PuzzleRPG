from scenes.game_scene import GameScene


class Director:
    def __init__(self):
        self.scenes = {}
        self.active_scene = None

    def compose(self):
        scene = GameScene()
        self.scenes[scene.tag] = scene

    def activate_scene(self, tag, game):
        self.active_scene = self.scenes[tag]
        self.active_scene.compose(game)
        self.active_scene.init(game)
        self.active_scene.start(game)

    def on_click(self, game, pos, cell):
        self.active_scene.on_click(game, pos, cell)

    def draw(self, game, surface):
        self.active_scene.draw(game, surface)

    def update(self, game, turn_type):
        self.active_scene.update(game, turn_type)
