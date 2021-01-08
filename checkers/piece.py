import pygame
from .constants import BLACK, WHITE, GREY, SQUARE_SIZE, B_KNIGHT, W_KNIGHT

class Piece:


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.img = None

        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2


    def draw(self, win):
        win.blit(self.img, (self.x - B_KNIGHT.get_width() // 2, self.y - B_KNIGHT.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(type(self).__name__)


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

        if self.color == WHITE:
            self.img = W_KNIGHT
        else:
            self.img = B_KNIGHT










