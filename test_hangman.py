from unittest import TestCase
from hangman import HangManGame


def create_assertion(string, tried, wrong_count):
    line = f"{string}\n"
    line += f"tried: {sorted(tried)}\n"
    line += f"wrong choices left: {wrong_count}\n"
    return line


class TestHangManGame(TestCase):
    def test_guess(self):
        game = HangManGame('networks')
        game.guess('n')
        actual = game.prompt()
        self.assertEqual(actual, create_assertion('n_______', {'n'}, 3))

    def test_guess_3(self):
        game = HangManGame('networks')
        game.guess('n')
        game.guess('e')
        game.guess('t')
        actual = game.prompt()
        self.assertEqual(
            actual,
            create_assertion('net_____', {'n', 'e', 't'}, 3)
        )

    def test_guess_all(self):
        game = HangManGame('networks')
        game.guess('n')
        game.guess('e')
        game.guess('t')
        game.guess('w')
        game.guess('o')
        game.guess('r')
        game.guess('k')
        game.guess('s')
        actual = game.prompt()
        self.assertEqual(
            actual,
            create_assertion(
                'networks',
                {'s', 'w', 't', 'o', 'k', 'e', 'r', 'n'},
                3
            )
        )
        self.assertTrue(game.is_game_over())
        self.assertTrue(game.has_found_all_letters())
