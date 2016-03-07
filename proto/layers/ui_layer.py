import globals
from core.layer import Layer
from entities.button import Button
from entities.label import Label


class UILayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def init(self, world):
        self.add_entity(Button((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 100), 'End turn'), 'btn_end')
        self.add_entity(Label((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 40), 'Status'), 'lbl_status')

    def update(self, world, turn):
        lbl = self.get_entity('lbl_status')
        lbl.text = 'Turn: %s' % turn

