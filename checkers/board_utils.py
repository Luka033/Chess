

NUM_TILES = 64
NUM_TILES_PER_ROW = 8

def init_column(column_number):
    column = [False] * NUM_TILES
    for i in range(column_number, len(column), NUM_TILES_PER_ROW):
        column[i] = True
    return column

def is_valid_tile_coordinate(coordinate):
    return (0 <= coordinate < NUM_TILES)


FIRST_COLUMN = init_column(0)
SECOND_COLUMN = init_column(1)
SEVENTH_COLUMN = init_column(6)
EIGHT_COLUMN = init_column(7)

SECOND_ROW = None
SEVENT_ROW = None

