import pygame
import abc
from .constants import BLACK, WHITE, SQUARE_SIZE, B_KNIGHT, W_KNIGHT, ROWS
from .board_utils import is_valid_tile_coordinate, FIRST_COLUMN, SECOND_COLUMN, SEVENTH_COLUMN, EIGHT_COLUMN

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
        # pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 5)
        win.blit(self.img, (col * SQUARE_SIZE + B_KNIGHT.get_width() // 2, row * SQUARE_SIZE + B_KNIGHT.get_height() // 2))
        # win.blit(self.img, (self.x - B_KNIGHT.get_width() // 2, self.y - B_KNIGHT.get_height() // 2))

    def move(self, row, col):
        self.tile_index = (ROWS * row + col)

    # Takes in the current board and the desired destination coordinate. Returns True if the tile is not occupied
    # by the same color Piece
    def not_occupied_by_ally(self, board, destination_coordinate):
        if board[destination_coordinate] != 0:
            return board[destination_coordinate].color == self.color
        return False

    def __repr__(self):
        return str(type(self).__name__)


class Knight(Piece):
    CANDIDATE_MOVE_COORDINATES = [-17, -15, -10, -6, 6, 10, 15, 17]

    def __init__(self, tile_index, color):
        super().__init__(tile_index, color)

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
                if self.__is_first_column_exclusion(idx, current_offset) or \
                        self.not_occupied_by_ally(board, destination_coordinate) or \
                        self.__is_second_column_exclusion(idx, current_offset) or \
                        self.__is_seventh_column_exclusion(idx, current_offset) or \
                        self.__is_eight_column_exclusion(idx, current_offset):
                    continue

                legal_moves.append(destination_coordinate)

        return legal_moves


    def __is_first_column_exclusion(self, current_position, candidate_offset):
        return FIRST_COLUMN[current_position] and (
                    candidate_offset == -17 or candidate_offset == -10 or
                    candidate_offset == 6 or candidate_offset == 15)

    def __is_second_column_exclusion(self, current_position, candidate_offset):
        return SECOND_COLUMN[current_position] and (
                    candidate_offset == -10 or candidate_offset == 6)

    def __is_seventh_column_exclusion(self, current_position, candidate_offset):
        return SEVENTH_COLUMN[current_position] and (
                    candidate_offset == -6 or candidate_offset == 10)

    def __is_eight_column_exclusion(self, current_position, candidate_offset):
        return EIGHT_COLUMN[current_position] and (
                    candidate_offset == -15 or candidate_offset == -6 or
                    candidate_offset == 10 or candidate_offset == 17)









