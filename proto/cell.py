class Cell:
    def __init__(self, row, column, content):
        self.row = row
        self.column = column
        self.content = content

    def move_up(self):
        return Cell(self.row - 2, self.column, self.content)

    def move_down(self):
        return Cell(self.row + 2, self.column, self.content)

    def move_up_right(self):
        return Cell(self.row - 1, self.column - 1, self.content)

    def move_up_left(self):
        return Cell(self.row - 1, self.column + 1, self.content)

    def move_down_left(self):
        return Cell(self.row + 1, self.column - 1, self.content)

    def move_down_right(self):
        return Cell(self.row + 1, self.column + 1, self.content)

    def get_round_bbox(self):
        yield self.move_up()
        yield self.move_down()
        yield self.move_up_left()
        yield self.move_up_right()
        yield self.move_down_left()
        yield self.move_down_right()
