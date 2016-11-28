from core.scene import Scene
from layers.editor_layer import EditorLayer
from layers.editor_ui_layer import EditorUILayer


class EditorScene(Scene):
    def __init__(self):
        Scene.__init__(self)

    def compose(self, game):
        self.add_layer(EditorLayer(0))
        self.add_layer(EditorUILayer(1))
