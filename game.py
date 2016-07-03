import math
import os
import pygame

import globals
from globals import TurnType
from core.observable import Observable
from core.director import Director


class Game(Observable):
    def __init__(self, surface, hex_map):
        Observable.__init__(self)
        self.surface = surface
        self.hex_map = hex_map
        self.director = Director()
        self.tiles = pygame.image.load(os.path.join('data', 'tiles.png')).convert_alpha()

    def init(self):
        self.director.compose()

    def start(self):
        self.camera_view = pygame.Rect(0, 0, globals.VIEW_WIDTH, globals.VIEW_HEIGHT)
        self.tod = [12, 0]
        self.tod_speed_min = globals.WORLD_TOD_SPEED_MIN
        self.turn = TurnType.PLAYER
        self.director.activate_scene('IntroScene', self)

    @property
    def scene(self):
        return self.director.active_scene

    def end_turn(self):
        if self.turn == TurnType.PLAYER:
            self.turn = TurnType.AI
            self.surface.set_alpha(100)
        else:
            self.turn = TurnType.PLAYER
            self.surface.set_alpha(255)
            self.update_tod()

    def update_tod(self):
        self.tod[1] += self.tod_speed_min
        if self.tod[1] >= 60:
            self.tod[1] -= 60
            self.tod[0] += 1
            if self.tod[0] >= 24:
                self.tod[0] = 0
        self.fire('on_tod_changed', game=self, hours=self.tod[0], minutes=self.tod[1])

    def is_in_camera(self, cell):
        if cell.row not in range(self.camera_view.top, self.camera_view.top + self.camera_view.height):
            return False
        if cell.column not in range(self.camera_view.left, self.camera_view.left + self.camera_view.width):
            return False
        return True

    def move_camera(self, cell):
        nr = pygame.Rect(0, 0, globals.VIEW_WIDTH, globals.VIEW_HEIGHT)
        nr = nr.move(cell.column - globals.CAMERA_COLUMN, cell.row - globals.CAMERA_ROW)
        if nr.top >= 0 and nr.left >= 0:
            if globals.WORLD_HEIGHT >= nr.top + globals.VIEW_HEIGHT:
                if globals.WORLD_WIDTH >= nr.left + globals.VIEW_WIDTH:
                    self.camera_view = nr

    def on_click(self, pos):
        cell = self.screen_to_cell(pos)
        self.director.on_click(self, pos, cell)

    def draw(self):
        self.director.draw(self, self.surface)

    def update(self):
        self.director.update(self, self.turn)

    def screen_to_cell(self, pos):
        view_row = 0
        for row in range(self.camera_view.top, self.camera_view.top + self.camera_view.height):
            view_col = 0
            for col in range(self.camera_view.left, self.camera_view.left + self.camera_view.width):
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
        for r in range(self.camera_view.top, self.camera_view.top + self.camera_view.height):
            view_col = 0
            for c in range(self.camera_view.left, self.camera_view.left + self.camera_view.width):
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

    def cell_to_ul_screen(self, cell):
        px, py = self.cell_to_screen(cell)
        return px - globals.HEX_RADIUS / 2, py - globals.HEX_RADIUS / 2
