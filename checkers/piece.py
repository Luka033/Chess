import pygame
import abc
from .constants import BLACK, WHITE, GREY, SQUARE_SIZE, B_KNIGHT, W_KNIGHT
from .board_utils import is_valid_tile_coordinate, FIRST_COLUMN, SECOND_COLUMN, SEVENTH_COLUMN, EIGHT_COLUMN

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

    @abc.abstractmethod
    def calculate_legal_moves(self, board):
        pass

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
    CANDIDATE_MOVE_COORDINATES = [-17, -15, -10, -6, 6, 10, 15, 17]

    def __init__(self, row, col, color):
        super().__init__(row, col, color)

        if self.color == WHITE:
            self.img = W_KNIGHT
        else:
            self.img = B_KNIGHT


    def calculate_legal_moves(self, board):
        legal_moves = []
        idx = board.index(self)

        for current_offset in self.CANDIDATE_MOVE_COORDINATES:
            destination_coordinate = idx + current_offset
            if is_valid_tile_coordinate(destination_coordinate):
                if self.isFirstColumnExclusion(idx, current_offset) or \
                        self.isSecondColumnExclusion(idx, current_offset) or \
                        self.isSeventhColumnExclusion(idx, current_offset) or \
                        self.isEighthColumnExclusion(idx, current_offset):
                    continue

                legal_moves.append(destination_coordinate)


        return legal_moves


                
    def isFirstColumnExclusion(self, current_position, candidate_offset):
        return FIRST_COLUMN[current_position] and (
                    candidate_offset == -17 or candidate_offset == -10 or
                    candidate_offset == 6 or candidate_offset == 15)


    def isSecondColumnExclusion(self, current_position, candidate_offset):
        return SECOND_COLUMN[current_position] and (
                    candidate_offset == -10 or candidate_offset == 6)

    def isSeventhColumnExclusion(self, current_position, candidate_offset):
        return SEVENTH_COLUMN[current_position] and (
                    candidate_offset == -6 or candidate_offset == 10)

    def isEighthColumnExclusion(self, current_position, candidate_offset):
        return EIGHT_COLUMN[current_position] and (
                    candidate_offset == -15 or candidate_offset == -6 or
                    candidate_offset == 10 or candidate_offset == 17)









