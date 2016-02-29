from core.layer import Layer
from world import TurnType


class AILayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def start(self, world):
        ui_layer = world.get_layer('UILayer')
        btn = ui_layer.get_entity('btn_end')
        btn.on_click = self.on_btn_end

    def on_btn_end(self, world):
        if world.turn == TurnType.PLAYER:
            return
        world.end_turn()

    def update(self, world, turn):
        ui_layer = world.get_layer('UILayer')
        lbl = ui_layer.get_entity('lbl_status')
        lbl.text = 'Turn: %s' % turn
