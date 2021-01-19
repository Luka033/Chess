import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


GREEN_BOX = pygame.transform.scale(pygame.image.load('assets/green_box.png'), (100, 100))
BG_BOARD = pygame.transform.scale(pygame.image.load('assets/chess_board.png'), (WIDTH, HEIGHT))
# Numbered board for debugging
# BG_BOARD = pygame.transform.scale(pygame.image.load('assets/numbered_bg.png'), (WIDTH, HEIGHT))

# Pieces
B_PAWN = pygame.image.load('assets/bP.png')
W_PAWN = pygame.image.load('assets/wP.png')

B_KNIGHT = pygame.image.load('assets/bN.png')
W_KNIGHT = pygame.image.load('assets/wN.png')

B_BISHOP = pygame.image.load('assets/bB.png')
W_BISHOP = pygame.image.load('assets/wB.png')

B_ROOK = pygame.image.load('assets/bR.png')
W_ROOK = pygame.image.load('assets/wR.png')

B_KING = pygame.image.load('assets/bK.png')
W_KING = pygame.image.load('assets/wK.png')

B_QUEEN = pygame.image.load('assets/bQ.png')
W_QUEEN = pygame.image.load('assets/wQ.png')


ALGEBRAIC_NOTATION = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
                      "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                      "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
                      "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
                      "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
                      "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
                      "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                      "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]

# For AI Evaluation
CHECK_BONUS = 50
CHECK_MATE_BONUS = 10000
DEPTH_BONUS = 100
CAPTURED_PIECE_BONUS = 20






















