import unittest
from game import Constants
from test import Objects


class TestRoom(unittest.TestCase):
    def test_room(self):
        room = Objects.TEST_ROOM
        expected = "This is a test room for testing. You see a test 2."
        self.assertEqual(expected, room.describe_room())

    def test_room_with_invisible_item(self):
        room = Objects.TEST_ROOM_2
        expected = "This is a test room 2 for testing. You see a test 2. You see a test ungettable."
        self.assertEqual(expected, room.describe_room())

    def test_room_with_person(self):
        room = Objects.TEST_ROOM_WITH_PERSON
        expected = "This is a test room for testing people. You see a test 2. You see Testman."
        self.assertEqual(expected, room.describe_room())

    def test_room_with_invisible_person(self):
        room = Objects.TEST_ROOM_WITH_INVISIBLE_PERSON
        expected = "This is a test room for testing people. You see a test 2."
        self.assertEqual(expected, room.describe_room())
