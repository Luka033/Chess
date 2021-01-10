import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


GREEN_BOX = pygame.transform.scale(pygame.image.load('assets/green_box.png'), (100, 100))
# BG_BOARD = pygame.transform.scale(pygame.image.load('assets/chess_board.png'), (WIDTH, HEIGHT))
BG_BOARD = pygame.transform.scale(pygame.image.load('assets/numbered_bg.png'), (WIDTH, HEIGHT))

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






















