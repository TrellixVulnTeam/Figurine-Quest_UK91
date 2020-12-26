import unittest
import Constants


class TestRoom(unittest.TestCase):
    def test_room(self):
        room = Constants.TEST_ROOM
        expected = "This is a test room for testing. You see a test 2."
        self.assertEqual(expected, room.describe_room())

    def test_room_with_invisible_item(self):
        room = Constants.TEST_ROOM_2
        expected = "This is a test room 2 for testing. You see a test 2. You see a test ungettable."
        self.assertEqual(expected, room.describe_room())
