from chess.board_utils import is_valid_tile_coordinate, piece_is_in_given_column
from chess.constants import WHITE, W_KNIGHT, B_KNIGHT
from chess.pieces.piece import Piece


class Knight(Piece):
    CANDIDATE_MOVE_COORDINATES = [-17, -15, -10, -6, 6, 10, 15, 17]

    def __init__(self, tile_index, color):
        super().__init__(tile_index, color)
        self.piece_value = 300
        self.notation = "N"
        if self.color == WHITE:
            self.img = W_KNIGHT
        else:
            self.img = B_KNIGHT


    def calculate_legal_moves(self, board):
        legal_moves = []
        piece_position = board.index(self)

        for current_offset in self.CANDIDATE_MOVE_COORDINATES:
            destination_coordinate = piece_position + current_offset
            if is_valid_tile_coordinate(destination_coordinate):
                if self.__is_first_column_exclusion(piece_position, current_offset) or \
                        self.is_tile_occupied_by_ally(board, destination_coordinate) or \
                        self.__is_second_column_exclusion(piece_position, current_offset) or \
                        self.__is_seventh_column_exclusion(piece_position, current_offset) or \
                        self.__is_eight_column_exclusion(piece_position, current_offset):
                    continue

                legal_moves.append(destination_coordinate)

        return legal_moves


    def __is_first_column_exclusion(self, current_position, candidate_offset):
        return piece_is_in_given_column(current_position, 0) and (
                    candidate_offset == -17 or candidate_offset == -10 or
                    candidate_offset == 6 or candidate_offset == 15)

    def __is_second_column_exclusion(self, current_position, candidate_offset):
        return piece_is_in_given_column(current_position, 1) and (
                    candidate_offset == -10 or candidate_offset == 6)

    def __is_seventh_column_exclusion(self, current_position, candidate_offset):
        return piece_is_in_given_column(current_position, 6) and (
                    candidate_offset == -6 or candidate_offset == 10)

    def __is_eight_column_exclusion(self, current_position, candidate_offset):
        return piece_is_in_given_column(current_position, 7) and (
                    candidate_offset == -15 or candidate_offset == -6 or
                    candidate_offset == 10 or candidate_offset == 17)