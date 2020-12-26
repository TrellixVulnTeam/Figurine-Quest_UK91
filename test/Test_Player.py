import unittest
import copy
from game import Constants
from test import Objects


class TestPlayer(unittest.TestCase):

    def test_inventory(self):
        player = copy.copy(Objects.TEST_PLAYER)
        print(player.get_inventory())
        self.assertEqual("You have: \ntest", player.get_inventory())

    def test_move_room(self):
        player = copy.copy(Objects.TEST_PLAYER)
        room = copy.copy(Objects.TEST_ROOM)
        room_two = copy.copy(Objects.TEST_ROOM_2)

        self.assertEqual(room.desc, player.location.desc)
        string = player.move_room("n")
        self.assertEqual(room_two.desc, player.location.desc)
        self.assertEqual(room_two.describe_room(), string)

    def test_move_room_with_invalid_move(self):
        player = copy.copy(Objects.TEST_PLAYER)
        room = copy.copy(Objects.TEST_ROOM)

        self.assertEqual(player.location.desc, room.desc)
        string = player.move_room("w")
        self.assertEqual(player.location.desc, room.desc)
        self.assertEqual(string, "You can't go that way.")
