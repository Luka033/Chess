import pygame
from .constants import BLACK, WHITE, ROWS, SQUARE_SIZE, WIDTH, GREEN_BOX, ALGEBRAIC_NOTATION
from chess.board import Board
from itertools import chain
from copy import deepcopy, copy

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
        self.check_mate = False
        self.large_font = pygame.font.SysFont("comicsans", 30)

    def update(self):
        self.board.draw(self.win)
        if self.selected:
            self.draw_valid_moves(self.valid_moves)
        # self.__display_text(f"Turn: {self.color_value.get(self.turn)}", WIDTH + 10, 10, (255, 255, 255))
        if self.check_mate:
            self.__display_text(f"Check Mate!! {self.color_value.get(self.__get_opposing_color())} Wins!!", 150, 350, (255, 0, 0))
            self.__display_text(f"Press R to restart", 300, 450, (255, 0, 0))
        pygame.display.update()

    def __display_text(self, text, x, y, color):
        text_label = self.large_font.render(f"{text}", 1, color)
        self.win.blit(text_label, (x, y))

    def reset(self):
        self._init()

    def __get_opposing_color(self):
        if self.turn == WHITE:
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
            if self.is_in_check(temp_board):
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

    def get_current_players_king_position(self, board):
        for i in range(len(board)):
            if str(board[i]) == 'King' and board[i].color == self.turn:
                return i
        return -1 # Should not happen


    '''
    Takes in a board and a king position. Calculates all the moves of the opposing player. Returns whether
    or not the given king position is in the list of opponent moves i.e. is in check
    '''
    def is_in_check(self, temp_board):
        temp_king_pos = self.get_current_players_king_position(temp_board)
        enemy_pieces = self.board.get_player_pieces(self.__get_opposing_color(), temp_board)
        current_enemy_moves = self.board.get_player_moves(enemy_pieces, temp_board)
        return temp_king_pos in current_enemy_moves

    def is_check_mate(self, board):
        # Get all current player pieces
        player_pieces = self.board.get_player_pieces(self.turn, board)
        # Use that to get all current player moves
        for piece in player_pieces:
            current_player_moves = piece.calculate_legal_moves(board)
            for move in current_player_moves:
                # make every move on the temporary board and return that board and king position
                _temp_board = self.simulate_move(piece, move, self.board.get_board().copy())
                # if on of the moves does not result in check i.e. there is a valid move, return false
                if not self.is_in_check(_temp_board):
                    return False
        return True

    '''
    Takes in a piece and destination coordinate, creates a copy of the current board and makes the move on the
    new board. Updates the king position if necessary. Returns the new board and the new king position.
    '''
    def simulate_move(self, piece, destination_coordinate, temp_board):
        # print(f"Piece: {piece}, Move: {destination_coordinate}")
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
            # print(self.selected.notation + ALGEBRAIC_NOTATION[coordinate])
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
            print("CHECK MATE!")
            self.check_mate = True


    def get_board(self):
        return self.board

    def ai_move(self, board):
        # print("Current: ", self.board.get_board())
        # print("Desired: ", board)
        current_board = self.board.get_board()
        piece = None
        coordinate = None

        for i in range(len(board)):
            if current_board[i] != board[i] and board[i] != 0:
                piece = board[i]
                coordinate = i
                break
        if piece:
            print(f"Piece: {piece}, Coord: {coordinate}")
            self.board.move(piece, coordinate)
        else:
            print("COULTND FIND PIECE")
        self.change_turn()


    def evaluate(self):
        score = 0
        if self.is_in_check(self.board.get_board()):
            score += 50
        if self.check_mate:
            score += 10000
        return 100








