import math
import globals


class MapView:
    def __init__(self, surface, hex_map, view_rect):
        self.surface = surface
        self.hex_map = hex_map
        self.view_rect = view_rect
        self.layers = []

    def is_in_view(self, cell):
        if cell.row not in xrange(self.view_rect.top, self.view_rect.top + self.view_rect.height):
            return False
        if cell.column not in xrange(self.view_rect.left, self.view_rect.left + self.view_rect.width):
            return False
        return True

    def on_click(self, pos):
        cell = self.screen_to_cell(pos)
        if cell:
            for layer in self.layers:
                layer.on_cell_click(self, cell)

    def draw(self):
        for layer in self.layers:
            layer.draw(self, self.surface)

    def screen_to_cell(self, pos):
        view_row = 0
        for row in xrange(self.view_rect.top, self.view_rect.top + self.view_rect.height):
            view_col = 0
            for col in xrange(self.view_rect.left, self.view_rect.left + self.view_rect.width):
                cell = self.hex_map.get_cell(row, col)
                if cell:
                    px = view_col * globals.HEX_RADIUS * 3 + view_row % 2 * (globals.HEX_RADIUS * 3 / 2)
                    py = view_row * globals.HEX_RADIUS * math.sqrt(3) / 2
                    view_col += 1

                    px += globals.VIEW_OFFSET[0]
                    py += globals.VIEW_OFFSET[1]
                    if math.pow(px - pos[0], 2) + math.pow(py - pos[1], 2) < math.pow(globals.HEX_RADIUS, 2):
                        return cell
            view_row += 1
        return None

    def cell_to_screen(self, cell):
        view_row = 0
        for r in xrange(self.view_rect.top, self.view_rect.top + self.view_rect.height):
            view_col = 0
            for c in xrange(self.view_rect.left, self.view_rect.left + self.view_rect.width):
                map_cell = self.hex_map.get_cell(r, c)
                if map_cell:
                    if map_cell.column == cell.column and map_cell.row == cell.row:
                        px = view_col * globals.HEX_RADIUS * 3 + view_row % 2 * (globals.HEX_RADIUS * 3 / 2)
                        py = view_row * globals.HEX_RADIUS * math.sqrt(3) / 2

                        px += globals.VIEW_OFFSET[0]
                        py += globals.VIEW_OFFSET[1]
                        return int(px), int(py)
                    view_col += 1
            view_row += 1
        return None
