import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 1  # 1 for 'X' (human) and -1 for 'O' (AI)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = 'X' if self.current_player == 1 else 'O'
            return True
        return False

    def check_winner(self):
        # Check rows for 'XXX' or 'OOO'
        for row in self.board:
            if row == ['X', 'X', 'X']:
                return 'X'
            elif row == ['O', 'O', 'O']:
                return 'O'

        # Check columns for 'XXX' or 'OOO'
        for col in range(3):
            if [self.board[0][col], self.board[1][col], self.board[2][col]] == ['X', 'X', 'X']:
                return 'X'
            elif [self.board[0][col], self.board[1][col], self.board[2][col]] == ['O', 'O', 'O']:
                return 'O'

        # Check diagonals for 'XXX' or 'OOO'
        if [self.board[0][0], self.board[1][1], self.board[2][2]] == ['X', 'X', 'X']:
            return 'X'
        elif [self.board[0][0], self.board[1][1], self.board[2][2]] == ['O', 'O', 'O']:
            return 'O'

        if [self.board[0][2], self.board[1][1], self.board[2][0]] == ['X', 'X', 'X']:
            return 'X'
        elif [self.board[0][2], self.board[1][1], self.board[2][0]] == ['O', 'O', 'O']:
            return 'O'

        return None  # No winner yet

    def is_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 1  # Reset to player X

    def ai_move(self):
        # Yapay zeka, kazanma fırsatını kontrol eder ve engelleme yapar
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'O'
                    if self.check_winner() == 'O':
                        return  # Eğer kazanıyorsa hamlesini yap ve çık
                    self.board[row][col] = ' '  # Hamle geri alın

        # Eğer insan oyuncunun kazanma fırsatı varsa, onu engelle
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'X'
                    if self.check_winner() == 'X':
                        self.board[row][col] = 'O'  # Engelle
                        return
                    self.board[row][col] = ' '  # Hamle geri alın

        # Eğer hiçbir kazanma veya engelleme yoksa, rastgele bir boş hücre seç
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)
