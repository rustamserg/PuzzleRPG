from core.scene import Scene
from layers.intro_layer import IntroLayer


class IntroScene(Scene):
    def __init__(self):
        Scene.__init__(self)

    def compose(self, game):
        self.add_layer(IntroLayer(0))
