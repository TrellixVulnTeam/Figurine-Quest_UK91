import unittest
import copy
from game import Player
from test import Objects


class TestPlayer(unittest.TestCase):

    def test_inventory(self):
        player = Player.Player(Objects.TEST_ROOM, [Objects.TEST_ITEM_IN_INVENTORY])
        self.assertEqual("You have: \ntest", player.get_inventory())

    def test_add_item(self):
        player = Player.Player(Objects.TEST_ROOM, [Objects.TEST_ITEM_IN_INVENTORY])
        player.add_item(Objects.TEST_ITEM_ON_GROUND)
        self.assertEqual("You have: \ntest\ntest 2", player.get_inventory())

    def test_remove_item(self):
        player = Player.Player(Objects.TEST_ROOM, [Objects.TEST_ITEM_IN_INVENTORY])
        player.remove_item(Objects.TEST_ITEM_IN_INVENTORY)
        self.assertEqual("You have: \n", player.get_inventory())

    def test_move_room(self):
        player = Player.Player(Objects.TEST_ROOM, [Objects.TEST_ITEM_IN_INVENTORY])
        room = copy.copy(Objects.TEST_ROOM)
        room_two = copy.copy(Objects.TEST_ROOM_2)

        self.assertEqual(room.desc, player.location.desc)
        string = player.move_room("n")
        self.assertEqual(room_two.desc, player.location.desc)
        self.assertEqual(room_two.describe_room(), string)

    def test_move_room_with_invalid_move(self):
        player = Player.Player(Objects.TEST_ROOM, [Objects.TEST_ITEM_IN_INVENTORY])
        room = copy.copy(Objects.TEST_ROOM)

        self.assertEqual(player.location.desc, room.desc)
        string = player.move_room("w")
        self.assertEqual(player.location.desc, room.desc)
        self.assertEqual(string, "You can't go that way.")
