import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
# BG_BOARD = pygame.transform.scale(pygame.image.load('assets/chess_board.png'), (WIDTH, HEIGHT))
BG_BOARD = pygame.transform.scale(pygame.image.load('assets/numbered_bg.png'), (WIDTH, HEIGHT))


B_KNIGHT = pygame.image.load('assets/bN.png')
W_KNIGHT = pygame.image.load('assets/wN.png')






















