import pygame
from .constants import BLACK, ROWS, COLS, SQUARE_SIZE, WHITE, BG_BOARD
from .piece import Piece, Knight

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 16

        self.create_board()

    def draw_squares(self, win):
        win.blit(BG_BOARD, (0, 0))

    def move(self, piece, row, col):
        self.board[ROWS * piece.row + piece.col], self.board[ROWS * row + col] = self.board[ROWS * row + col], self.board[ROWS * piece.row + piece.col]

        # self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[ROWS * row + col]
        # return self.board[row][col]

    def get_board(self):
        return self.board

    def create_board(self):
        # self.board = [[0, Knight(0, 1, WHITE), 0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board = [0, 0, 0, 0, 0, 0, 0, 0,
                      Knight(1, 0, WHITE), 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, Knight(3, 4, WHITE), 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0]



    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[ROWS * row + col]
                if piece != 0:
                    piece.draw(win)











