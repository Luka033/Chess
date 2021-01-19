from copy import deepcopy
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)




def minimax(position, depth, max_player, game):
    if depth == 0 or game.check_mate:
        return game.evaluate(depth, position), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move
        return min_eval, best_move


def get_all_moves(board, color, game):
    moves = []
    player_pieces = [piece for piece in board if piece != 0 and piece.color != color]

    for piece in player_pieces:
        current_player_moves = piece.calculate_legal_moves(board)
        for move in current_player_moves:
            # make every move on the temporary board and return that board and king position
            temp_board = board.copy()
            new_board = game.simulate_move(piece, move, temp_board)
            if not game.is_in_check(new_board, color):
                moves.append(new_board)
    return moves


