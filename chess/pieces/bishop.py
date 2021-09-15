from chess.board_utils import is_valid_tile_coordinate, piece_is_in_given_column
from chess.constants import WHITE, W_BISHOP, B_BISHOP
from chess.pieces.piece import Piece


class Bishop(Piece):
    CANDIDATE_MOVE_COORDINATES = [-9, -7, 7, 9]

    def __init__(self, tile_index, color):
        super().__init__(tile_index, color)
        self.piece_value = 400
        if self.color == WHITE:
            self.img = W_BISHOP
        else:
            self.img = B_BISHOP


    def calculate_legal_moves(self, board):
        legal_moves = []
        piece_position = board.index(self)

        for current_offset in self.CANDIDATE_MOVE_COORDINATES:
            destination_coordinate = piece_position

            while(is_valid_tile_coordinate(destination_coordinate)):
                if self.__is_first_column_exclusion(destination_coordinate, current_offset) or \
                    self.__is_eight_column_exclusion(destination_coordinate, current_offset):
                    break

                destination_coordinate += current_offset
                if is_valid_tile_coordinate(destination_coordinate):
                    if not self.is_tile_occupied(board, destination_coordinate):
                        legal_moves.append(destination_coordinate)
                    else:
                        if not self.is_tile_occupied_by_ally(board, destination_coordinate):
                            legal_moves.append(destination_coordinate)
                        break

        return legal_moves


    def __is_first_column_exclusion(self, current_position, candidate_offset):
        return piece_is_in_given_column(current_position, 0) and (candidate_offset == -9 or candidate_offset == 7)

    def __is_eight_column_exclusion(self, current_position, candidate_offset):
        return piece_is_in_given_column(current_position, 7) and (candidate_offset == -7 or candidate_offset == 9)