from items.item import Item


class TestItem01(Item):
    def __init__(self, cell):
        Item.__init__(self, cell, 'test_item_01', 'test_item_01')
