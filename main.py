import pygame
from chess.constants import WIDTH, HEIGHT, SQUARE_SIZE, BG_BOARD
from chess.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH + 200, HEIGHT))
pygame.display.set_caption('Chess')


# def display_test(text, x, y):
#     title_label = title_font.render(text, 1, (255, 255, 255))
#     WIN.blit(title_label, (x - title_label.get_width() // 2, y - title_label.get_height() // 2))

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # print(f"Row: {row}, Col: {col}")
                if col <= 7:
                    game.select(row, col)

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