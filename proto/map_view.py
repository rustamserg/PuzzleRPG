import math
import globals


class MapView:
    def __init__(self, surface, hex_map, view_rect):
        self.surface = surface
        self.hex_map = hex_map
        self.view_rect = view_rect

    def on_click(self, pos):
        target_cell = self.screen_to_cell(pos)
        if target_cell:
            for row in xrange(self.view_rect.top, self.view_rect.top + self.view_rect.height):
                for col in xrange(self.view_rect.left, self.view_rect.left + self.view_rect.width):
                    cell = self.hex_map.get_cell(row, col)
                    if cell:
                        cell.on_cell_click(target_cell)

    def draw(self):
        view_row = 0
        for row in xrange(self.view_rect.top, self.view_rect.top + self.view_rect.height):
            view_col = 0
            for col in xrange(self.view_rect.left, self.view_rect.left + self.view_rect.width):
                cell = self.hex_map.get_cell(row, col)
                if cell:
                    cell.draw(self.surface)
                    view_col += 1
            view_row += 1

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

    def cell_to_screen(self, row, column):
        view_row = 0
        for r in xrange(self.view_rect.top, self.view_rect.top + self.view_rect.height):
            view_col = 0
            for c in xrange(self.view_rect.left, self.view_rect.left + self.view_rect.width):
                cell = self.hex_map.get_cell(r, c)
                if cell:
                    if cell.column == column and cell.row == row:
                        px = view_col * globals.HEX_RADIUS * 3 + view_row % 2 * (globals.HEX_RADIUS * 3 / 2)
                        py = view_row * globals.HEX_RADIUS * math.sqrt(3) / 2

                        px += globals.VIEW_OFFSET[0]
                        py += globals.VIEW_OFFSET[1]
                        return int(px), int(py)
                    view_col += 1
            view_row += 1
        return None
