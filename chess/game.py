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

    def update(self):
        self.board.draw(self.win)
        if self.selected:
            self.draw_valid_moves(self.valid_moves)
        self.__display_text(f"Turn: {self.color_value.get(self.turn)}", WIDTH + 10, 10, (255, 255, 255), 30)
        if self.check_mate:
            self.__display_text(f"Check Mate!! {self.color_value.get(self.turn)} Wins!!", 250, 350, (255, 0, 0), 70)
            self.__display_text(f"Press R to restart", 300, 350, (255, 0, 0), 50)
        pygame.display.update()

    def __display_text(self, text, x, y, color, size):
        self.main_font = pygame.font.SysFont("comicsans", size)
        text_label = self.main_font.render(f"{text}", 1, color)
        self.win.blit(text_label, (x, y))

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []
        self.white_king_pos = 60
        self.black_king_pos = 1
        self.check_mate = False

    def reset(self):
        self._init()

    def __get_opposing_color(self):
        if self.turn == WHITE:
            return BLACK
        else:
            return WHITE

    def __get_player_pieces(self, color, temp_board):
        enemy_pieces = []
        for piece in temp_board:
            if piece != 0 and piece.color != color:
                enemy_pieces.append(piece)
        return enemy_pieces

    def get_player_moves(self, pieces, temp_board):
        # all_moves = set()
        # for piece in pieces:
        #     all_moves.update(piece.calculate_legal_moves(temp_board))
        # return list(all_moves)
        # print("Pieces: ", pieces)
        all_moves = {}
        for piece in pieces:
            all_moves[piece] = piece.calculate_legal_moves(temp_board)
        return all_moves

    def get_current_players_king_position(self):
        if self.turn == WHITE:
            return self.white_king_pos
        else:
            return self.black_king_pos

    def is_in_check(self, temp_board, temp_king_pos):
        enemy_pieces = self.__get_player_pieces(self.turn, temp_board)
        current_enemy_moves = self.get_player_moves(enemy_pieces, temp_board)
        return temp_king_pos in list(chain(*current_enemy_moves.values()))
        # return temp_king_pos in current_enemy_moves

    def is_check_mate(self, board):
        # player_pieces = [piece for piece in board if piece != 0 and piece.color == self.turn]
        # current_player_moves = self.get_player_moves(player_pieces, board)
        # piece = player_pieces[0]
        # _temp_board, temp_king_pos = self.try_move(piece, list(current_player_moves.values())[0][0])



        player_pieces = [piece for piece in board if piece != 0 and piece.color == self.turn]
        current_player_moves = self.get_player_moves(player_pieces, board)
        print(current_player_moves)
        for piece in current_player_moves.keys():
            for move in current_player_moves.get(piece):
                _temp_board, temp_king_pos = self.try_move(piece, move)
                if not self.is_in_check(_temp_board, temp_king_pos):
                    return False
        return True

    def try_move(self, piece, destination_coordinate):
        temp_king_pos = self.get_current_players_king_position()
        temp_board = self.board.get_board().copy()
        piece_position = piece.tile_index
        temp_board[destination_coordinate] = piece
        temp_board[piece_position] = 0
        if str(piece) == "King":
            temp_king_pos = destination_coordinate

        return temp_board, temp_king_pos

    def select(self, row, col):
        if self.selected:
            destination_coordinate = (ROWS * row + col)
            temp_board, temp_king_pos = self.try_move(self.selected, destination_coordinate)
            if self.is_in_check(temp_board, temp_king_pos):
                self.selected = None
                self.select(row, col)


            result = self.__move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = piece.calculate_legal_moves(self.board.get_board())
                return True

        return False

    def update_king_pos(self, position):
        if self.turn == WHITE:
            self.white_king_pos = position
        else:
            self.black_king_pos = position


    def __move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and (ROWS * row + col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            if str(self.selected) == "King":
                self.update_king_pos((ROWS * row + col))
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
            if self.is_in_check(self.board.get_board(), self.white_king_pos):
                print("CHECK!")
                # TODO: Check if checkmate
                if self.is_check_mate(self.board.get_board()):
                    print("CHECK MATE!")
                    self.check_mate = True
        else:
            self.turn = BLACK
            if self.is_in_check(self.board.get_board(), self.black_king_pos):
                print("CHECK!")
                # TODO: Check if checkmate
                if self.is_check_mate(self.board.get_board()):
                    print("CHECK MATE!")
                    self.check_mate = True




