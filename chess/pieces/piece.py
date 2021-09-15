import abc
from chess.constants import WHITE, BLACK, SQUARE_SIZE, B_KNIGHT, ROWS


class Piece:
    def __init__(self, tile_index, color):
        self.tile_index = tile_index
        self.color = color
        self.img = None
        self.notation = str(self)[:1]
        self.direction = -1 if self.color == BLACK else 1

    @abc.abstractmethod
    def calculate_legal_moves(self, board):
        pass

    def draw(self, win):
        row = self.tile_index // ROWS
        col = self.tile_index % ROWS
        win.blit(self.img, (col * SQUARE_SIZE + B_KNIGHT.get_width() // 2 - 10, row * SQUARE_SIZE + B_KNIGHT.get_height() // 2 - 10))

    def move(self, coordinate):
        self.tile_index = coordinate

    def is_tile_occupied_by_ally(self, board, coordinate):
        if self.is_tile_occupied(board, coordinate):
            return board[coordinate].color == self.color
        return False

    def is_tile_occupied(self, board, coordinate):
        return board[coordinate] != 0

    def __repr__(self):
        return str(type(self).__name__)









