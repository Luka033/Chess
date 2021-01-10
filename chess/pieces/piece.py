import abc
from chess.constants import BLACK, SQUARE_SIZE, B_KNIGHT, ROWS


class Piece:
    def __init__(self, tile_index, color):
        self.tile_index = tile_index
        self.color = color
        self.img = None

        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1

    @abc.abstractmethod
    def calculate_legal_moves(self, board):
        pass

    def draw(self, win):
        row = self.tile_index // ROWS
        col = self.tile_index % ROWS
        win.blit(self.img, (col * SQUARE_SIZE + B_KNIGHT.get_width() // 2 - 10, row * SQUARE_SIZE + B_KNIGHT.get_height() // 2 - 10))

    def move(self, row, col):
        self.tile_index = (ROWS * row + col)

    # Takes in the current board and the desired destination coordinate. Returns True if the tile is not occupied
    # by the same color Piece
    def occupied_by_ally(self, board, destination_coordinate):
        if board[destination_coordinate] != 0:
            return board[destination_coordinate].color == self.color
        return False

    def __repr__(self):
        return str(type(self).__name__)









