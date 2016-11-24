from core.scene import Scene
from layers.editor_layer import EditorLayer


class EditorScene(Scene):
    def __init__(self):
        Scene.__init__(self)

    def compose(self, game):
        self.add_layer(EditorLayer(0))
