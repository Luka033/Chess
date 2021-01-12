from chess.board_utils import is_valid_tile_coordinate, piece_is_in_given_column
from chess.constants import WHITE, W_KING, B_KING
from chess.pieces.piece import Piece


class King(Piece):
    CANDIDATE_MOVE_COORDINATES = [-9, -8, -7, -1, 1, 7, 8, 9]

    def __init__(self, tile_index, color):
        super().__init__(tile_index, color)

        if self.color == WHITE:
            self.img = W_KING
        else:
            self.img = B_KING


    def calculate_legal_moves(self, board):
        legal_moves = []
        piece_position = board.index(self)

        for current_offset in self.CANDIDATE_MOVE_COORDINATES:
            destination_coordinate = piece_position + current_offset
            if is_valid_tile_coordinate(destination_coordinate):
                if self.__is_first_column_exclusion(piece_position, current_offset) or \
                        self.is_tile_occupied_by_ally(board, destination_coordinate) or \
                        self.__is_eight_column_exclusion(piece_position, current_offset):
                    continue

                legal_moves.append(destination_coordinate)

        return legal_moves


    def __is_first_column_exclusion(self, current_position, candidate_offset):
        return piece_is_in_given_column(current_position, 0) and (candidate_offset == -9 or candidate_offset == -1 or candidate_offset == 7)


    def __is_eight_column_exclusion(self, current_position, candidate_offset):
        return piece_is_in_given_column(current_position, 7) and (candidate_offset == -7 or candidate_offset == 1 or candidate_offset == 9)