from .constants import BLACK, ROWS, COLS, WHITE, BG_BOARD
from .pieces.knight import Knight
from .pieces.bishop import Bishop
from .pieces.rook import Rook
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.pawn import Pawn


class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 16

        self.create_board()

    def draw_squares(self, win):
        win.blit(BG_BOARD, (0, 0))

    def move(self, piece, row, col):
        idx = self.board.index(piece)
        self.board[ROWS * row + col] = piece
        self.board[idx] = 0

        piece.move(row, col)
        # # Debugging
        # for i in range(0, len(self.board), 8):
        #     print(self.board[i: i+8])


    def get_piece(self, row, col):
        return self.board[ROWS * row + col]

    def get_board(self):
        return self.board

    def create_board(self):
        self.board = [Rook(0, BLACK), Knight(1, BLACK), Bishop(2, BLACK), Queen(3, BLACK), King(4, BLACK), Bishop(5, BLACK), Knight(6, BLACK), Rook(7, BLACK),
                      Pawn(8, BLACK), Pawn(9, BLACK), Pawn(10, BLACK), Pawn(11, BLACK), Pawn(12, BLACK), Pawn(13, BLACK), Pawn(14, BLACK), Pawn(15, BLACK),
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      Pawn(48, WHITE), Pawn(49, WHITE), Pawn(50, WHITE), Pawn(51, WHITE), Pawn(52, WHITE), Pawn(53, WHITE), Pawn(54, WHITE), Pawn(55, WHITE),
                      Rook(56, WHITE), Knight(57, WHITE), Bishop(58, WHITE), Queen(59, WHITE), King(60, WHITE), Bishop(61, WHITE), Knight(62, WHITE), Rook(63, WHITE)]


    def draw(self, win):
        win.fill(BLACK)
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[ROWS * row + col]
                if piece != 0:
                    piece.draw(win)












