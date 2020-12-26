import unittest
import copy
from game import Commands, Constants, Item, Player, Room
from test import Objects


class MyTestCase(unittest.TestCase):
    def test_move_command_valid_move(self):
        user_input = "north"
        player = copy.copy(Objects.TEST_PLAYER)
        room = copy.copy(Objects.TEST_ROOM)
        room_two = copy.copy(Objects.TEST_ROOM_2)
        self.assertEqual(player.location.desc, room.desc)
        Commands.parse_move_command(user_input, player)
        self.assertEqual(player.location.desc, room_two.desc)

    def test_move_command_invalid_move(self):
        user_input = "west"
        player = copy.copy(Objects.TEST_PLAYER)
        room = copy.copy(Objects.TEST_ROOM)
        self.assertEqual(player.location.desc, room.desc)
        actual = Commands.parse_move_command(user_input, player)
        self.assertEqual(Constants.EXIT_NOT_FOUND_STRING, actual)

    def test_help_command(self):
        actual = Commands.parse_help_command()
        self.assertEqual(Constants.PLAYER_HELP, actual)

    def test_quit_command(self):
        self.assertEqual(True, True)
        # TODO: Add this

    def test_look_command(self):
        player = copy.copy(Objects.TEST_PLAYER)
        actual = Commands.parse_look_command(player)
        self.assertEqual(player.location.desc, actual)

    def test_examine_command_item_in_room(self):
        user_input = ["examine", "test 2"]
        player = copy.copy(Objects.TEST_PLAYER)
        actual = Commands.parse_examine_command(user_input, player)
        self.assertEqual(Objects.TEST_ITEM_ON_GROUND.long_desc, actual)

    def test_examine_command_item_in_inventory(self):
        user_input = ["examine", "test"]
        player = copy.copy(Objects.TEST_PLAYER)
        actual = Commands.parse_examine_command(user_input, player)
        self.assertEqual(Objects.TEST_ITEM_IN_INVENTORY.long_desc, actual)

    def test_examine_command_item_not_found(self):
        user_input = ["examine", "test not present"]
        player = copy.copy(Objects.TEST_PLAYER)
        expected = Constants.ITEM_NOT_VISIBLE_STRING + "test not present."
        actual = Commands.parse_examine_command(user_input, player)
        self.assertEqual(expected, actual)

    def test_take_command_item_in_room(self):
        user_input = ["take", "test 2"]
        item = Item.Item("test 2", "Short desc 2", "Long desc 2", True, True)
        room = Room.Room("Test Room", "This is a test room for testing.", {}, [item], [])
        player = Player.Player(room, [Objects.TEST_ITEM_IN_INVENTORY])

        self.assertTrue(item in room.items)
        self.assertTrue(item not in player.inventory)

        actual = Commands.parse_take_command(user_input, player)
        self.assertTrue(item not in room.items)
        self.assertTrue(item in player.inventory)
        self.assertTrue("You take the test 2.", actual)

    def test_take_command_item_not_present(self):
        user_input = ["take", "test not present"]
        player = copy.copy(Objects.TEST_PLAYER)
        room = Room.Room("Test Room", "This is a test room for testing.", {}, [Objects.TEST_ITEM_ON_GROUND], [])
        item = copy.copy(Objects.TEST_ITEM_NOT_PRESENT)

        self.assertTrue(item not in room.items)
        self.assertTrue(item not in player.inventory)

        actual = Commands.parse_take_command(user_input, player)
        self.assertTrue(item not in room.items)
        self.assertTrue(item not in player.inventory)
        self.assertTrue(Constants.ITEM_NOT_VISIBLE_STRING, actual)
