import pygame
from .constants import BLACK, WHITE, ROWS, SQUARE_SIZE, GREEN_BOX
from .constants import CHECK_BONUS, DEPTH_BONUS, CAPTURED_PIECE_BONUS, CHECK_MATE_BONUS, ALGEBRAIC_NOTATION
from chess.board import Board




pygame.font.init()

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
        self.large_font = pygame.font.SysFont("comicsans", 50)
        self.small_font = pygame.font.SysFont("comicsans", 18)
        self.move_x, self.move_y = 805, 40
        self.__draw_static_text()

    def __draw_static_text(self):
        self.win.fill(BLACK)
        self.__display_text(self.small_font, 'WHITE | BLACK | WHITE | BLACK', 800, 20, (255, 255, 255))

    def update(self):
        self.board.draw(self.win)
        if self.selected:
            self.draw_valid_moves(self.valid_moves)
        if self.check_mate:
            self.__display_text(self.large_font, f"Check Mate!! {self.color_value.get(self.turn)} Wins!!", 250, 350, (255, 0, 0))
            self.__display_text(self.large_font, "Press R to restart", 300, 450, (255, 0, 0))
        pygame.display.update()

    def __display_moves(self, move):
        if self.turn == WHITE:
            self.__display_text(self.small_font, move, self.move_x, self.move_y, (255, 255, 255))
        else:
            self.__display_text(self.small_font, move, self.move_x + 50, self.move_y, (255, 255, 255))
            self.move_y += 20

        if self.move_y > 780:
            self.move_x = 905


    def __display_text(self, font, text, x, y, color):
        text_label = font.render(f"{text}", 1, color)
        self.win.blit(text_label, (x, y))

    def reset(self):
        self._init()

    def __get_opposing_color(self, color):
        if color == WHITE:
            return BLACK
        else:
            return WHITE

    '''
    Takes in a coordinate, if a piece is selected it will make the move on a temporary board to ensure it is valid.
    Otherwise a piece will be selected and its valid moves will be calculated
    '''
    def select(self, coordinate):
        if self.selected:
            destination_coordinate = coordinate
            temp_board = self.simulate_move(self.selected, destination_coordinate, self.board.get_board().copy())
            if self.is_in_check(temp_board, self.__get_opposing_color(self.turn)):
                print("CHECK!!!")
                self.selected = None
                self.select(coordinate)

            result = self.__move(coordinate)
            if not result:
                self.selected = None
                self.select(coordinate)
        else:
            piece = self.board.get_piece(coordinate)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = piece.calculate_legal_moves(self.board.get_board())
                return True

        return False

    def get_king_position(self, board, color):
        for i in range(len(board)):
            if str(board[i]) == 'King' and board[i].color == color:
                return i
        return -1 # Should not happen

    '''
    Takes in a board and a king position. Calculates all the moves of the opposing player. Returns whether
    or not the given king position is in the list of opponent moves i.e. is in check
    '''
    def is_in_check(self, temp_board, color):
        temp_king_pos = self.get_king_position(temp_board, self.__get_opposing_color(color))
        enemy_pieces = self.board.get_player_pieces(color, temp_board)
        current_enemy_moves = self.board.get_player_moves(enemy_pieces, temp_board)

        return temp_king_pos in current_enemy_moves

    def is_check_mate(self, board, color):
        # Get all current player pieces
        player_pieces = self.board.get_player_pieces(color, board)
        # Use that to get all current player moves
        for piece in player_pieces:
            current_player_moves = piece.calculate_legal_moves(board)
            for move in current_player_moves:
                # make every move on the temporary board and return that board and king position
                _temp_board = self.simulate_move(piece, move, board.copy())
                # if on of the moves does not result in check i.e. there is a valid move, return false
                if not self.is_in_check(_temp_board, self.__get_opposing_color(color)):
                    return False
        return True

    '''
    Takes in a piece and destination coordinate, creates a copy of the current board and makes the move on the
    new board. Updates the king position if necessary. Returns the new board and the new king position.
    '''
    def simulate_move(self, piece, destination_coordinate, temp_board):
        piece_position = piece.tile_index
        temp_board[destination_coordinate] = piece
        temp_board[piece_position] = 0
        return temp_board

    '''
    Takes in a coordinate and ensured the coordinate is one of the valid moves. If true the move will be made.
    If the move was made by the kind then the king position will be updated. Returns false otherwise.
    '''
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
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

        if self.is_check_mate(self.board.get_board(), self.turn):
            self.check_mate = True


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


    '''
    Evaluates a given board using the helper functions below
    '''
    def evaluate(self, depth, board):
        return self.__check(board) + self.__checkmate(depth, board) + self.__mobility() + self.__piece_value(board)

    def __checkmate(self, depth, board):
        return CHECK_MATE_BONUS * self.__depth_bonus(depth) if self.is_check_mate(board, self.__get_opposing_color(self.turn)) else 0

    def __depth_bonus(self, depth):
        return 1 if depth == 0 else DEPTH_BONUS * depth

    def __check(self, board):
        return CHECK_BONUS if self.is_in_check(board, self.turn) else 0

    def __mobility(self):
        return len(self.valid_moves)

    def __piece_value(self, board):
        piece_value_score = 0
        pieces = self.board.get_player_pieces(self.turn, board)
        for piece in pieces:
            piece_value_score += piece.piece_value
        return piece_value_score








