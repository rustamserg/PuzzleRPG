import pygame
import math


class MapView:
    def __init__(self, back, hex_map, view, offset):
        self.background = back
        self.hex_map = hex_map
        self.view = view
        self.offset = offset

    def draw(self):
        view_row = 0
        for row in xrange(self.view.top, self.view.top + self.view.height):
            view_col = 0
            for col in xrange(self.view.left, self.view.left + self.view.width):
                cell = self.hex_map.get_cell(row, col)
                if cell:
                    points = []
                    px = view_col * self.hex_map.radius * 3 + view_row % 2 * (self.hex_map.radius * 3 / 2)
                    py = view_row * self.hex_map.radius * math.sqrt(3) / 2
                    view_col += 1
                    for ang in range(6):
                        x = px + self.hex_map.radius * math.cos(math.radians((ang + 1) * 60))
                        y = py + self.hex_map.radius * math.sin(math.radians((ang + 1) * 60))
                        points.append([x + self.offset.x, y + self.offset.y])
                    pygame.draw.polygon(self.background, cell.content, points)
                    pygame.draw.polygon(self.background, pygame.Color(0, 0, 0), points, 2)
            view_row += 1

    def screen_to_cell(self, pos):
        view_row = 0
        for row in xrange(self.view.left, self.view.left + self.view.height):
            view_col = 0
            for col in xrange(self.view.top, self.view.top + self.view.width):
                cell = self.hex_map.get_cell(col, row)
                if cell:
                    px = view_col * self.hex_map.radius * 3 + view_row % 2 * (self.hex_map.radius * 3 / 2)
                    py = view_row * self.hex_map.radius * math.sqrt(3) / 2
                    px += self.offset.x
                    py += self.offset.y
                    if math.pow(px - pos.x, 2) + math.pow(py - pos.y, 2) < math.pow(self.hex_map.radius, 2):
                        return cell
            view_row += 1
        return None
