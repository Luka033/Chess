import pygame
from .constants import BLACK, ROWS, COLS, SQUARE_SIZE, WHITE, BG_BOARD
from .piece import Piece, Knight

class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 16

        self.create_board()

    def draw_squares(self, win):
        win.blit(BG_BOARD, (0, 0))

    def move(self, piece, row, col):
        # self.board[ROWS * piece.row + piece.col], self.board[ROWS * row + col] = self.board[ROWS * row + col], self.board[ROWS * piece.row + piece.col]
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
        self.board = [0, 0, 0, 0, 0, 0, Knight(6, WHITE), 0,
                      Knight(8, WHITE), 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, Knight(28, BLACK), 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, Knight(62, BLACK), 0]



    def draw(self, win):
        win.fill(BLACK)
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[ROWS * row + col]
                if piece != 0:
                    piece.draw(win)












