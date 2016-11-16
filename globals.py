class TurnType:
    def __init__(self):
        pass

    AI = 'AI'
    PLAYER = 'Player'


WORLD_WIDTH = 100
WORLD_HEIGHT = 100
WORLD_TOD_SPEED_MIN = 10

VIEW_WIDTH = 14
VIEW_HEIGHT = 14
VIEW_OFFSET = (110, 100)
HEX_RADIUS = 30

CAMERA_COLUMN = int(VIEW_WIDTH / 2)
CAMERA_ROW = int(VIEW_HEIGHT / 2)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

INVENTORY_WIDTH = 9
INVENTORY_HEIGHT = 5
INVENTORY_CELL_SIZE = 64

PLAYER_HUNGER_SPEED = 2