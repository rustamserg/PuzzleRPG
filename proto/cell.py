class Cell:
    def __init__(self, row, column, content):
        self.row = row
        self.column = column
        self.content = content

    def draw(self, surface, px, py):
        for entity in self.content:
            entity.draw(surface, px, py)

    def get_round_bbox(self):
        yield Cell(self.row - 2, self.column, self.content)
        yield Cell(self.row + 2, self.column, self.content)
        yield Cell(self.row - 1, self.column - 1, self.content)
        yield Cell(self.row - 1, self.column + 1, self.content)
        yield Cell(self.row + 1, self.column - 1, self.content)
        yield Cell(self.row + 1, self.column + 1, self.content)
