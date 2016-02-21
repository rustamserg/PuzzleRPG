class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.column == self.column and other.row == self.row

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def up(cell):
        return Cell(cell.row - 2, cell.column)

    @staticmethod
    def up_right(cell):
        return Cell(cell.row - 1, cell.column + 1)

    @staticmethod
    def up_left(cell):
        return Cell(cell.row - 1, cell.column - 1)

    @staticmethod
    def down(cell):
        return Cell(cell.row + 2, cell.column)

    @staticmethod
    def down_right(cell):
        return Cell(cell.row + 1, cell.column + 1)

    @staticmethod
    def down_left(cell):
        return Cell(cell.row + 1, cell.column - 1)

    @staticmethod
    def round_bbox(cell):
        yield Cell.up(cell)
        yield Cell.up_right(cell)
        yield Cell.down_right(cell)
        yield Cell.down(cell)
        yield Cell.down_left(cell)
        yield Cell.up_left(cell)