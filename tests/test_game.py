import unittest
from src.game import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_make_move(self):
        game = TicTacToe()
        game.make_move(0, 0, 1)
        self.assertEqual(game.board[0, 0], 1)

    def test_check_winner(self):
        game = TicTacToe()
        game.make_move(0, 0, 1)
        game.make_move(0, 1, 1)
        game.make_move(0, 2, 1)
        self.assertTrue(game.check_winner())

if __name__ == '__main__':
    unittest.main()
