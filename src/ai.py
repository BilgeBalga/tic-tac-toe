import random

class RandomAI:
    def make_move(self, board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]
        return random.choice(empty_cells) if empty_cells else None

def minimax(board, depth, is_maximizing):
    if board.check_winner():
        return 1 if is_maximizing else -1
    if board.is_draw():
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    board[i, j] = 1  # AI player
                    score = minimax(board, depth + 1, False)
                    board[i, j] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    board[i, j] = -1  # User player
                    score = minimax(board, depth + 1, True)
                    board[i, j] = 0
                    best_score = min(score, best_score)
        return best_score
