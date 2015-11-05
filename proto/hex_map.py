from cell import Cell


class HexMap:
    def __init__(self, width, height):
        self.cells = []
        self.radius = 25
        self.height = height
        self.width = width
        self.init_map()

    def init_map(self):
        for row in range(self.height):
            self.cells.append([])
            for column in range(self.width):
                if row % 2 == 0 and column % 2 != 0:
                    self.cells[row].append(None)
                elif row % 2 != 0 and column % 2 == 0:
                    self.cells[row].append(None)
                else:
                    self.cells[row].append(Cell(row, column, 0))

    def get_cell(self, row, column):
        if 0 <= row < self.height:
            if 0 <= column < self.width:
                return self.cells[row][column]
        return None
