
import unittest
from unittest.mock import patch
from io import StringIO
import random

# Assuming your game code is in a file named 'rps_game.py'

# Import the functions from the game code
from main import get_user_choice, determine_winner, play_again, rock_paper_scissors

class TestRockPaperScissorsGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['r'])
    def test_get_user_choice(self, mock_input):
        self.assertEqual(get_user_choice(), 'r')

    def test_determine_winner_player_wins(self):
        self.assertEqual(determine_winner('r', 's'), "You won! Rock crushes Scissors.")

    def test_determine_winner_opponent_wins(self):
        self.assertEqual(determine_winner('s', 'r'), "You lost. Rock does not beat Scissors.")

    def test_determine_winner_tie(self):
        self.assertEqual(determine_winner('p', 'p'), "It's a Tie!")

    @patch('builtins.input', side_effect=['yes'])
    def test_play_again_yes(self, mock_input):
        self.assertTrue(play_again())

    @patch('builtins.input', side_effect=['no'])
    def test_play_again_no(self, mock_input):
        self.assertFalse(play_again())

    @patch('builtins.input', side_effect=['r'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_rock_paper_scissors(self, mock_stdout, mock_input):
        # Redirect stdout for testing printed output
        rock_paper_scissors()
        output = mock_stdout.getvalue().strip()
        # Add assertions based on your expected output

if __name__ == '__main__':
    unittest.main()


