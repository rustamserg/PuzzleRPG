from core.scene import Scene
from layers.ai_layer import AILayer
from layers.ground_layer import GroundLayer
from layers.player_layer import PlayerLayer
from layers.ui_layer import UILayer
from layers.inventory_layer import InventoryLayer
from layers.items_layer import ItemsLayer
from layers.script_layer import ScriptLayer


class GameScene(Scene):
    def __init__(self):
        Scene.__init__(self)

    def compose(self, game):
        self.add_layer(GroundLayer(0))
        self.add_layer(ItemsLayer(1))
        self.add_layer(AILayer(2))
        self.add_layer(PlayerLayer(3))
        self.add_layer(UILayer(4))
        self.add_layer(InventoryLayer(5))
        self.add_layer(ScriptLayer(6))
