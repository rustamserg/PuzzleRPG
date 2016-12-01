class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.ground = None
        self.item = None

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.column == self.column and other.row == self.row

    def __ne__(self, other):
        return not self.__eq__(other)
