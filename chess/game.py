import pygame
from .constants import BLACK, WHITE, ROWS, SQUARE_SIZE, GREEN_BOX
from .constants import CHECK_BONUS, DEPTH_BONUS, CHECK_MATE_BONUS, ALGEBRAIC_NOTATION, LARGE_FONT, SMALL_FONT
from chess.board import Board
from chess.board_utils import display_text

class Game:
    def __init__(self, win):
        self.win = win
        self.color_value = {(255, 255, 255): "White", (0, 0, 0): "Black"}
        self._init()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []
        self.check_mate = False
        self.move_x, self.move_y = 805, 40
        self.__draw_static_text()

    def __draw_static_text(self):
        self.win.fill(BLACK)
        display_text(self.win, SMALL_FONT, 'WHITE | BLACK | WHITE | BLACK', 800, 20, (255, 255, 255))

    def update(self):
        self.board.draw(self.win)
        if self.selected:
            self.draw_valid_moves(self.valid_moves)
        if self.check_mate:
            display_text(self.win, LARGE_FONT, f"Check Mate!! {self.color_value.get(self.turn)} Wins!!", 250, 350, (255, 0, 0))
            display_text(self.win, LARGE_FONT, "Press R to restart", 300, 450, (255, 0, 0))
        pygame.display.update()

    def __display_moves(self, move):
        if self.turn == WHITE:
            display_text(self.win, SMALL_FONT, move, self.move_x, self.move_y, (255, 255, 255))
        else:
            display_text(self.win, SMALL_FONT, move, self.move_x + 50, self.move_y, (255, 255, 255))
            self.move_y += 20

        if self.move_y > 780:
            self.move_x = 905

    def reset(self):
        self._init()

    def __get_opposing_color(self, color):
        return BLACK if color == WHITE else WHITE

    def select(self, coordinate):
        """
        Takes in a coordinate, if a piece is selected it will make the move on a temporary board to ensure it is valid.
        Otherwise a piece will be selected and its valid moves will be calculated
        :param coordinate: integer representing the selected board coordinate
        :return: boolean representing whether or not a piece has been selected
        """
        if self.selected:
            destination_coordinate = coordinate
            temp_board = self.simulate_move(self.selected, destination_coordinate, self.board.get_board().copy())
            if self.is_in_check(temp_board, self.__get_opposing_color(self.turn)):
                self.selected = None
                self.select(coordinate)

            result = self.__move(coordinate)
            if not result:
                self.selected = None
                self.select(coordinate)
            else:
                self.update()
        else:
            piece = self.board.get_piece(coordinate)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = piece.calculate_legal_moves(self.board.get_board())
                return True

        return False

    def get_king_position(self, current_board, color):
        for i in range(len(current_board)):
            if str(current_board[i]) == 'King' and current_board[i].color == color:
                return i
        return -1 # Should not happen

    def is_in_check(self, current_board, color):
        temp_king_pos = self.get_king_position(current_board, self.__get_opposing_color(color))
        enemy_pieces = self.board.get_player_pieces(color, current_board)
        current_enemy_moves = self.board.get_player_moves(enemy_pieces, current_board)

        return temp_king_pos in current_enemy_moves

    def is_check_mate(self, current_board, color):
        player_pieces = self.board.get_player_pieces(color, current_board)
        for piece in player_pieces:
            current_player_moves = piece.calculate_legal_moves(current_board)
            for move in current_player_moves:
                updated_board = self.simulate_move(piece, move, current_board.copy())
                # if one of the moves does not result in check i.e. there is a valid move, return false
                if not self.is_in_check(updated_board, self.__get_opposing_color(color)):
                    return False
        return True


    def simulate_move(self, piece, destination_coordinate, simulated_board):
        piece_position = piece.tile_index
        simulated_board[destination_coordinate] = piece
        simulated_board[piece_position] = 0
        return simulated_board


    def __move(self, coordinate):
        if self.selected and coordinate in self.valid_moves:
            self.board.move(self.selected, coordinate)
            self.__display_moves(self.selected.notation + ALGEBRAIC_NOTATION[coordinate])
            self.change_turn()
        else:
            return False
        return True


    def draw_valid_moves(self, moves):
        for move in moves:
            row = move // ROWS
            col = move % ROWS
            self.win.blit(GREEN_BOX, (col * SQUARE_SIZE, row * SQUARE_SIZE))


    def change_turn(self):
        self.selected = None
        self.turn = WHITE if self.turn == BLACK else BLACK

        if self.is_check_mate(self.board.get_board(), self.turn):
            self.check_mate = True

    def get_current_player(self):
        return self.turn

    def get_board(self):
        return self.board

    def ai_move(self, board):
        current_board = self.board.get_board()
        piece = None
        coordinate = None

        # Find the Piece that was moved and its coordinate
        for i in range(len(board)):
            if current_board[i] != board[i] and board[i] != 0:
                piece = board[i]
                coordinate = i
                break
        if piece:
            self.__display_moves(piece.notation + ALGEBRAIC_NOTATION[coordinate])
            self.board.move(piece, coordinate)
        else:
            print("COULDN'T FIND PIECE")
        self.change_turn()


    def evaluate(self, depth, current_board):
        """
        Evaluates a given board using the helper functions below
        :param depth: integer representing how deep the minimax algorithm went
        :param current_board:
        :return: inteer representing the evaluated score
        """
        return self.__check(current_board) + self.__checkmate(depth, current_board) + self.__mobility() + self.__piece_value(current_board)

    def __checkmate(self, depth, current_board):
        return CHECK_MATE_BONUS * self.__depth_bonus(depth) if self.is_check_mate(current_board, self.__get_opposing_color(self.turn)) else 0

    def __depth_bonus(self, depth):
        return 1 if depth == 0 else DEPTH_BONUS * depth

    def __check(self, current_board):
        return CHECK_BONUS if self.is_in_check(current_board, self.__get_opposing_color(self.turn)) else 0

    def __mobility(self):
        return len(self.valid_moves)

    def __piece_value(self, current_board):
        piece_value_score = 0
        pieces = self.board.get_player_pieces(self.turn, current_board)
        for piece in pieces:
            piece_value_score += piece.piece_value
        return piece_value_score








