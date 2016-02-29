from core.layer import Layer


class LogicLayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def start(self, world):
        ui_layer = world.get_layer('UILayer')
        btn = ui_layer.get_entity('btn_end')
        btn.set_on_click(lambda w: w.end_turn())

    def update(self, world, turn):
        ui_layer = world.get_layer('UILayer')
        lbl = ui_layer.get_entity('lbl_status')
        lbl.text = 'Turn: %s' % turn
