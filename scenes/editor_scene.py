from core.scene import Scene
from layers.editor_layer import EditorLayer
from layers.editor_ui_layer import EditorUILayer
from layers.items_layer import ItemsLayer
from layers.script_layer import ScriptLayer


class EditorScene(Scene):
    def __init__(self):
        Scene.__init__(self)

    def compose(self, game):
        self.add_layer(EditorLayer(0))
        self.add_layer(EditorUILayer(1))
        self.add_layer(ItemsLayer(2))
        self.add_layer(ScriptLayer(3))
