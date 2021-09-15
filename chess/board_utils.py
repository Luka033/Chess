from chess.constants import ROWS, COLS, NUM_TILES, SQUARE_SIZE


# Takes in a piece position and a row number. NOTE that the row is on a 0 index scale so row 1 = 0, row 2 = 1 etc
def piece_is_in_given_row(piece_position, row):
    return (piece_position // ROWS) == row

# Takes in a piece position and a column number. NOTE that the col is on a 0 index scale so col 1 = 0, col 2 = 1 etc
def piece_is_in_given_column(piece_position, col):
    return (piece_position % COLS) == col

def is_valid_tile_coordinate(coordinate):
    return (0 <= coordinate < NUM_TILES)

def display_text(win, font, text, x, y, color):
    text_label = font.render(f"{text}", 1, color)
    win.blit(text_label, (x, y))

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col




