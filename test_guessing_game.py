# test_bot_player.py
import unittest
from unittest.mock import patch
from bot_player import BotPlayer

class TestBotPlayer(unittest.TestCase):

    def test_correct_guess(self):
        bot = BotPlayer(1, 100)
        secret = 42
        guess = None
        while guess != secret:
            guess = bot.make_guess()
            if guess < secret:
                bot.update("higher")
            elif guess > secret:
                bot.update("lower")
        self.assertEqual(guess, secret)

    def test_narrows_higher(self):
        bot = BotPlayer(1, 100)
        first = bot.make_guess()
        bot.update("higher")
        second = bot.make_guess()
        self.assertGreater(second, first)

    def test_narrows_lower(self):
        bot = BotPlayer(1, 100)
        first = bot.make_guess()
        bot.update("lower")
        second = bot.make_guess()
        self.assertLess(second, first)

    @patch('bot_player.BotPlayer.make_guess', return_value=42)
    def test_mocked_guess(self, mock_guess):
        bot = BotPlayer()
        guess = bot.make_guess()
        self.assertEqual(guess, 42)
        mock_guess.assert_called_once()

if __name__ == '__main__':
    unittest.main()
