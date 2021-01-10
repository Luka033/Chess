from chess.constants import ROWS, COLS

NUM_TILES = 64
NUM_TILES_PER_ROW = 8

def init_column(column_number):
    column = [False] * NUM_TILES
    for i in range(column_number, len(column), NUM_TILES_PER_ROW):
        column[i] = True
    return column

def init_row(row_number):
    row = [False] * 64
    for i in range(row_number, row_number + 8):
        row[i] = True

    return row

# Takes in a piece position and a row number. NOTE that the row is on a 0 index scale so row 1 = 0, row 2 = 1 etc
def piece_is_in_given_row(piece_position, row):
    return (piece_position // ROWS) == row

# Takes in a piece position and a column number. NOTE that the col is on a 0 index scale so col 1 = 0, col 2 = 1 etc
def piece_is_in_given_column(piece_position, col):
    return (piece_position % COLS) == col

def is_valid_tile_coordinate(coordinate):
    return (0 <= coordinate < NUM_TILES)


FIRST_COLUMN = init_column(0)
SECOND_COLUMN = init_column(1)
SEVENTH_COLUMN = init_column(6)
EIGHT_COLUMN = init_column(7)

SECOND_RANK = init_row(8)
SEVENTH_RANK = init_row(48)



