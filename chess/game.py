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
        turn_label = {(255, 255, 255): "White", (0, 0, 0): "Black"}
        level_label = self.main_font.render(f"Turn: {turn_label.get(self.turn)}", 1, (255, 255, 255))
        self.win.blit(level_label, (WIDTH, 10))

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
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


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and (ROWS * row + col) in self.valid_moves:
            self.board.move(self.selected, row, col)
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