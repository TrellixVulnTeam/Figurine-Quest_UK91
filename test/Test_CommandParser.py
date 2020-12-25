import unittest
import CommandParser
import Constants
import copy


class TestCommandParser(unittest.TestCase):

    def test_invalid_commands(self):
        user_inputs = ["InvalidCommand", "Invalid Command", "Invalid Triple Command"]
        player = copy.copy(Constants.TEST_PLAYER)

        for user_input in user_inputs:
            actual = CommandParser.parse_input(user_input, player)
            self.assertEqual(Constants.INVALID_COMMAND_GIVEN_STRING, actual)

    def test_help_command(self):
        user_input = "help"
        player = copy.copy(Constants.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        self.assertEqual(Constants.PLAYER_HELP, actual)