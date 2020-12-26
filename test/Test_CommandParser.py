import unittest
from game import CommandParser, Constants
import copy
from test import Objects


class TestCommandParser(unittest.TestCase):

    def test_invalid_single_word_command(self):
        user_input = "InvalidCommand"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        self.assertEqual(Constants.INVALID_COMMAND_GIVEN_STRING, actual)

    def test_invalid_two_word_command(self):
        user_input = "Invalid Command"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        self.assertEqual(Constants.INVALID_COMMAND_GIVEN_STRING, actual)

    def test_invalid_three_word_command(self):
        user_input = "Invalid Triple Command"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        self.assertEqual(Constants.INVALID_COMMAND_GIVEN_STRING, actual)

    def test_help_command(self):
        user_input = "help"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        self.assertEqual(Constants.PLAYER_HELP, actual)

    def test_look_command(self):
        user_input = "look"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        self.assertEqual(Objects.TEST_ROOM.desc, actual)

    def test_examine_command_item_on_ground(self):
        user_input = "examine test 2"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        self.assertEqual(Objects.TEST_ITEM_ON_GROUND.long_desc, actual)

    def test_examine_command_item_in_inventory(self):
        user_input = "examine test"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        self.assertEqual(Objects.TEST_ITEM_IN_INVENTORY.long_desc, actual)

    def test_examine_command_item_not_present(self):
        user_input = "examine test not present"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        expected = Constants.ITEM_NOT_VISIBLE_STRING + "test not present."
        self.assertEqual(expected, actual)

    def test_take_command_item_on_ground(self):
        user_input = "take test 2"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        expected = Constants.ITEM_TAKEN_STRING + Objects.TEST_ITEM_ON_GROUND.name + '.'
        self.assertEqual(expected, actual)

    def test_take_command_item_in_inventory(self):
        user_input = "take test"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        expected = Constants.ITEM_NOT_VISIBLE_STRING + Objects.TEST_ITEM_IN_INVENTORY.name + '.'
        self.assertEqual(expected, actual)

    def test_take_command_item_not_present(self):
        user_input = "take test not present"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        expected = Constants.ITEM_NOT_VISIBLE_STRING + Objects.TEST_ITEM_NOT_PRESENT.name + '.'
        self.assertEqual(expected, actual)

    def test_take_command_item_not_takeable(self):
        user_input = "take test ungettable"
        player = copy.copy(Objects.TEST_PLAYER_2)
        actual = CommandParser.parse_input(user_input, player)
        expected = Constants.ITEM_NOT_TAKEABLE_STRING + Objects.TEST_ITEM_NO_GET.name + '.'
        self.assertEqual(expected, actual)

    def test_talk_command_person_present(self):
        user_input = "talk testman"
        player = copy.copy(Objects.TEST_PLAYER_IN_PERSON_ROOM)
        actual = CommandParser.parse_input(user_input, player)
        expected = Constants.BASE_DIALOGUE
        self.assertEqual(expected, actual)

    def test_talk_command_person_invisible(self):
        user_input = "talk testman"
        player = copy.copy(Objects.TEST_PLAYER_IN_INVISIBLE_PERSON_ROOM)
        actual = CommandParser.parse_input(user_input, player)
        expected = Constants.PERSON_NOT_VISIBLE_STRING + 'testman.'
        self.assertEqual(expected, actual)

    def test_talk_command_person_not_present(self):
        user_input = "talk testman"
        player = copy.copy(Objects.TEST_PLAYER)
        actual = CommandParser.parse_input(user_input, player)
        expected = Constants.PERSON_NOT_VISIBLE_STRING + 'testman.'
        self.assertEqual(expected, actual)
