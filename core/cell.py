class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.layers = {}

    @property
    def ground(self):
        return self.layers['ground']

    @property
    def item(self):
        return self.layers['item'] if 'item' in self.layers.keys() else None

    @property
    def script(self):
        return self.layers['script'] if 'script' in self.layers.keys() else None

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.column == self.column and other.row == self.row

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "%i_%i" % (self.row, self.column)
