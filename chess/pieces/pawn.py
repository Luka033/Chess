from chess.board_utils import is_valid_tile_coordinate, piece_is_in_given_row, piece_is_in_given_column
from chess.constants import WHITE, BLACK, W_PAWN, B_PAWN
from chess.pieces.piece import Piece


class Pawn(Piece):
    CANDIDATE_MOVE_COORDINATES = [8, 16, 7, 9]

    def __init__(self, tile_index, color):
        super().__init__(tile_index, color)
        self.piece_value = 100
        if self.color == WHITE:
            self.img = W_PAWN
            self.direction = -1
        else:
            self.img = B_PAWN
            self.direction = 1


    def calculate_legal_moves(self, board):
        legal_moves = []
        piece_position = board.index(self)

        for current_offset in self.CANDIDATE_MOVE_COORDINATES:
            destination_coordinate = piece_position + (self.direction * current_offset)
            if not is_valid_tile_coordinate(destination_coordinate):
                continue

            if current_offset == 8 and not self.is_tile_occupied(board, destination_coordinate):
                # TODO: PAWN promotion square
                legal_moves.append(destination_coordinate)


            # # TODO: ADD first move check (maybe not needed because of row check)
            elif current_offset == 16 and \
                    (piece_is_in_given_row(piece_position, 6) and self.color == WHITE or
                     piece_is_in_given_row(piece_position, 1) and self.color == BLACK):
                behind_candidate_destination_coordinate = piece_position + (self.direction * 8)
                if not self.is_tile_occupied(board, behind_candidate_destination_coordinate) and \
                    not self.is_tile_occupied(board, destination_coordinate):
                    legal_moves.append(destination_coordinate)

            elif current_offset == 7 and not \
                    (piece_is_in_given_column(piece_position, 7) and self.color == WHITE or
                     piece_is_in_given_column(piece_position, 0) and self.color == BLACK):
                if self.is_tile_occupied(board, destination_coordinate):
                    piece_on_candidate = board[destination_coordinate]
                    if self.color != piece_on_candidate.color:
                        # TODO: Add promotion square
                        legal_moves.append(destination_coordinate)

                # elif TODO: Add enpassantPawn

            elif current_offset == 9 and not \
                    (piece_is_in_given_column(piece_position, 0) and self.color == WHITE or
                     piece_is_in_given_column(piece_position, 7) and self.color == BLACK):
                if self.is_tile_occupied(board, destination_coordinate):
                    piece_on_candidate = board[destination_coordinate]
                    if self.color != piece_on_candidate.color:
                        # TODO: Add promotion square
                        legal_moves.append(destination_coordinate)
                # elif TODO: Add enpassantPawn

        return legal_moves



