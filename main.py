import pygame
from chess.constants import WIDTH, HEIGHT, SQUARE_SIZE, ROWS, BLACK
from chess.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH + 200, HEIGHT))
pygame.display.set_caption('Chess')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    DEPTH = 3


    while run:
        clock.tick(FPS)

        if game.turn == BLACK:
            value, new_board = minimax(game.board.get_board(), DEPTH, BLACK, game)
            game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)

                if col <= 7:
                    game.select((8 * row + col))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game.reset()

        game.update()
    pygame.quit()


main()


# if __name__ == '__main__':
#     title_font = pygame.font.SysFont("comicsans", 50)
#     run = True
#     while run:
#         WIN.blit(BG_BOARD, (0, 0))
#
#         display_test("Press 1 to play AI", 350, 250)
#         display_test("Press 2 for two player", 350, 350)
#         display_test("Press R at any time to restart", 350, 450)
#
#
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             keys = pygame.key.get_pressed()
#             if keys[pygame.K_1]:
#                 main()
#
#     pygame.quit()