import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                move_from_row, move_from_col = get_row_col_from_mouse(pos)
                print(f"Row from: {move_from_row}, Col from: {move_from_col}")
                # print(board.get_board())
                piece = board.get_piece(move_from_row, move_from_col)
                print(piece.calculate_legal_moves(board.get_board()))
                # board.move(piece, 4, 3)

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()
