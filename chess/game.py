import pygame
from .constants import BLACK, WHITE, ROWS, GREEN, SQUARE_SIZE, WIDTH, GREEN_BOX
from chess.board import Board
from itertools import chain

pygame.font.init()

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.color_value = {(255, 255, 255): "White", (0, 0, 0): "Black"}

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []
        self.white_king_pos = 60
        self.black_king_pos = 4
        self.check_mate = False

    def update(self):
        self.board.draw(self.win)
        if self.selected:
            self.draw_valid_moves(self.valid_moves)
        self.__display_text(f"Turn: {self.color_value.get(self.turn)}", WIDTH + 10, 10, (255, 255, 255), 30)
        if self.check_mate:
            self.__display_text(f"Check Mate!! {self.color_value.get(self.__get_opposing_color())} Wins!!", 150, 350, (255, 0, 0), 70)
            self.__display_text(f"Press R to restart", 300, 450, (255, 0, 0), 50)
        pygame.display.update()

    def __display_text(self, text, x, y, color, size):
        self.main_font = pygame.font.SysFont("comicsans", size)
        text_label = self.main_font.render(f"{text}", 1, color)
        self.win.blit(text_label, (x, y))

    def reset(self):
        self._init()

    def __get_opposing_color(self):
        if self.turn == WHITE:
            return BLACK
        else:
            return WHITE

    '''
    Returns all pieces of the given color on the given board
    '''
    def __get_player_pieces(self, color, temp_board):
        pieces = [piece for piece in temp_board if piece != 0 and piece.color == color]
        return pieces

    '''
    Takes in a list of pieces and a board. Returns a dictionary where keys are pieces and values are the
    corresponding legal moves
    '''
    def __get_player_moves(self, pieces, temp_board):
        all_moves = {}
        for piece in pieces:
            all_moves[piece] = piece.calculate_legal_moves(temp_board)
        return all_moves

    def get_current_players_king_position(self):
        if self.turn == WHITE:
            return self.white_king_pos
        else:
            return self.black_king_pos

    '''
    Takes in a board and a king position. Calculates all the moves of the opposing player. Returns whether
    or not the given king position is in the list of opponent moves i.e. is in check
    '''
    def is_in_check(self, temp_board, temp_king_pos):
        enemy_pieces = self.__get_player_pieces(self.__get_opposing_color(), temp_board)
        current_enemy_moves = self.__get_player_moves(enemy_pieces, temp_board)
        return temp_king_pos in list(chain(*current_enemy_moves.values()))


    def is_check_mate(self, board):
        # Get all current player pieces
        player_pieces = self.__get_player_pieces(self.turn, board)
        # Use that to get all current player moves
        current_player_moves = self.__get_player_moves(player_pieces, board)
        for piece in current_player_moves.keys():
            for move in current_player_moves.get(piece):
                # make every move on the temporary board and return that board and king position
                _temp_board, temp_king_pos = self.make_test_move(piece, move)
                # if on of the moves does not result in check i.e. there is a valid move, return false
                if not self.is_in_check(_temp_board, temp_king_pos):
                    return False
        return True

    '''
    Takes in a piece and destination coordinate, creates a copy of the current board and makes the move on the
    new board. Updates the king position if necessary. Returns the new board and the new king position.
    '''
    def make_test_move(self, piece, destination_coordinate):
        temp_king_pos = self.get_current_players_king_position()
        temp_board = self.board.get_board().copy()
        piece_position = piece.tile_index
        temp_board[destination_coordinate] = piece
        temp_board[piece_position] = 0
        if str(piece) == "King":
            temp_king_pos = destination_coordinate

        return temp_board, temp_king_pos

    '''
    Takes in a coordinate, if a piece is selected it will make the move on a temporary board to ensure it is valid.
    Otherwise a piece will be selected and its valid moves will be calculated
    '''
    def select(self, coordinate):
        if self.selected:
            destination_coordinate = coordinate
            temp_board, temp_king_pos = self.make_test_move(self.selected, destination_coordinate)
            if self.is_in_check(temp_board, temp_king_pos):
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


    '''
    Takes in a tile position and updates the king position of the current player
    '''
    def update_king_pos(self, position):
        if self.turn == WHITE:
            self.white_king_pos = position
        else:
            self.black_king_pos = position

    '''
    Takes in a coordinate and ensured the coordinate is one of the valid moves. If true the move will be made.
    If the move was made by the kind then the king position will be updated. Returns false otherwise.
    '''
    def __move(self, coordinate):
        if self.selected and coordinate in self.valid_moves:
            self.board.move(self.selected, coordinate)
            if str(self.selected) == "King":
                self.update_king_pos(coordinate)
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

        if self.is_check_mate(self.board.get_board()):
            # print("CHECK MATE!")
            self.check_mate = True






