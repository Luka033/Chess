from .constants import BLACK, ROWS, COLS, WHITE, BG_BOARD
from .pieces.knight import Knight
from .pieces.bishop import Bishop
from .pieces.rook import Rook
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.pawn import Pawn
from chess.board_utils import piece_is_in_given_row


class Board:
    def __init__(self):
        self.board = []
        self.__create_board()

    def draw_grid(self, win):
        win.blit(BG_BOARD, (0, 0))

    def draw(self, win):
        self.draw_grid(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[ROWS * row + col]
                if piece != 0:
                    piece.draw(win)

    def get_player_moves(self, pieces, current_board):
        """
        :param pieces: list of pieces
        :param current_board: array representing the current board
        :return: dictionary where keys are pieces and values are the corresponding legal moves
        """
        all_moves = set()
        for piece in pieces:
            all_moves.update(piece.calculate_legal_moves(current_board))

        return list(all_moves)

    def get_player_pieces(self, color, current_board):
        """
        :param color: the color to get pieces for
        :param current_board: array representing the current board
        :return: list of all pieces of the given color on the given board
        """
        pieces = [piece for piece in current_board if piece != 0 and piece.color == color]
        return pieces

    def move(self, piece, coordinate):
        piece_position = self.board.index(piece)
        self.board[coordinate] = piece
        self.board[piece_position] = 0
        piece.move(coordinate)

        if str(piece) == "Pawn":
            self.__pawn_promotion(piece)

    def __pawn_promotion(self, pawn_piece):
        """
        Promotes the given pawn piece to a queen if it appears in the first opposing row
        :param pawn_piece: pawn piece tp be promoted
        :return:
        """
        if piece_is_in_given_row(pawn_piece.tile_index, 0) and pawn_piece.color == WHITE:
            self.board[pawn_piece.tile_index] = Queen(pawn_piece.tile_index, WHITE)
        if piece_is_in_given_row(pawn_piece.tile_index, 7) and pawn_piece.color == BLACK:
            self.board[pawn_piece.tile_index] = Queen(pawn_piece.tile_index, BLACK)

    def get_piece(self, coordinate):
        return self.board[coordinate]

    def get_board(self):
        return self.board

    def __create_board(self):
        self.board = [Rook(0, BLACK), Knight(1, BLACK), Bishop(2, BLACK), Queen(3, BLACK), King(4, BLACK),
                      Bishop(5, BLACK), Knight(6, BLACK), Rook(7, BLACK),
                      Pawn(8, BLACK), Pawn(9, BLACK), Pawn(10, BLACK), Pawn(11, BLACK), Pawn(12, BLACK),
                      Pawn(13, BLACK), Pawn(14, BLACK), Pawn(15, BLACK),
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      Pawn(48, WHITE), Pawn(49, WHITE), Pawn(50, WHITE), Pawn(51, WHITE), Pawn(52, WHITE),
                      Pawn(53, WHITE), Pawn(54, WHITE), Pawn(55, WHITE),
                      Rook(56, WHITE), Knight(57, WHITE), Bishop(58, WHITE), Queen(59, WHITE), King(60, WHITE),
                      Bishop(61, WHITE), Knight(62, WHITE), Rook(63, WHITE)]

        """
        Boards for debugging and quick testing
        """
        # self.board = [0, King(1, BLACK), 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               Rook(56, WHITE), Knight(57, WHITE), Bishop(58, WHITE), Queen(59, WHITE), King(60, WHITE),
        #               Bishop(61, WHITE), Knight(62, WHITE), Rook(63, WHITE)]

        # self.board = [Rook(0, BLACK), Knight(1, BLACK), Bishop(2, BLACK), Queen(3, BLACK), King(4, BLACK),
        #               Bishop(5, BLACK), Knight(6, BLACK), Rook(7, BLACK),
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, King(60, WHITE),
        #               0, 0, 0]

        # self.board = [Rook(0, BLACK), Knight(1, BLACK), Bishop(2, BLACK), Queen(3, BLACK), King(4, BLACK),
        #               Bishop(5, BLACK), Knight(6, BLACK), Rook(7, BLACK),
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               0, 0, 0, 0, 0, 0, 0, 0,
        #               Rook(56, WHITE), Knight(57, WHITE), Bishop(58, WHITE), Queen(59, WHITE), King(60, WHITE),
        #               Bishop(61, WHITE), Knight(62, WHITE), Rook(63, WHITE)]
