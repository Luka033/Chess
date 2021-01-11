import pygame
from .constants import BLACK, WHITE, ROWS, GREEN, SQUARE_SIZE, WIDTH, GREEN_BOX
from chess.board import Board

pygame.font.init()

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.main_font = pygame.font.SysFont("comicsans", 30)

    def update(self):
        self.board.draw(self.win)
        self._draw_turn()
        if self.selected:
            self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _draw_turn(self):
        turn_value = {(255, 255, 255): "White", (0, 0, 0): "Black"}
        turn_label = self.main_font.render(f"Turn: {turn_value.get(self.turn)}", 1, (255, 255, 255))
        self.win.blit(turn_label, (WIDTH + 10, 10))

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []
        self.white_king_pos = 60
        self.black_king_pos = 4

    def reset(self):
        self._init()

    def __get_enemy_pieces(self, color, temp_board):
        enemy_pieces = []
        for piece in temp_board:
            if piece != 0 and piece.color != color:
                enemy_pieces.append(piece)
        return enemy_pieces

    def get_all_enemy_moves(self, pieces, temp_board):
        all_moves = set()
        for piece in pieces:
            all_moves.update(piece.calculate_legal_moves(temp_board))
        return list(all_moves)

    def get_current_players_king_position(self):
        if self.turn == WHITE:
            return self.white_king_pos
        else:
            return self.black_king_pos

    def is_in_check(self, temp_board, temp_king_pos):
        enemy_pieces = self.__get_enemy_pieces(self.turn, temp_board)
        current_enemy_moves = self.get_all_enemy_moves(enemy_pieces, temp_board)
        return temp_king_pos in current_enemy_moves

    def is_check_mate(self, temp_board):
        pass

    def try_move(self, destination_coordinate):
        temp_king_pos = self.get_current_players_king_position()
        temp_board = self.board.get_board().copy()
        piece_position = self.selected.tile_index
        temp_board[destination_coordinate] = self.selected
        temp_board[piece_position] = 0
        if str(self.selected) == "King":
            temp_king_pos = destination_coordinate

        return temp_board, temp_king_pos

    def select(self, row, col):
        if self.selected:
            destination_coordinate = (ROWS * row + col)
            temp_board, temp_king_pos = self.try_move(destination_coordinate)
            if self.is_in_check(temp_board, temp_king_pos):
                # TODO: Check if checkmate
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
                # for move in self.valid_moves:
                #     if move in self.current_enemy_moves:
                #         self.valid_moves.remove(move)

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
            # pygame.draw.rect(self.win, GREEN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
            self.win.blit(GREEN_BOX, (col * SQUARE_SIZE, row * SQUARE_SIZE))


    def change_turn(self):
        self.selected = None
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

        # print("Check: ", self.is_in_check())