import unittest

from game.content import Test_Objects


class TestRoom(unittest.TestCase):
    def test_room(self):
        room = Test_Objects.TEST_ROOM
        expected = "Test Room\nThis is a test room for testing. You see a test 2."
        self.assertEqual(expected, room.describe_room())

    def test_room_with_invisible_item(self):
        room = Test_Objects.TEST_ROOM_2
        expected = "Test Room 2\nThis is a test room 2 for testing. You see a test 2. You see a test ungettable."
        self.assertEqual(expected, room.describe_room())

    def test_room_with_person(self):
        room = Test_Objects.TEST_ROOM_WITH_PERSON
        expected = "Test Room With Person\nThis is a test room for testing people. You see a test 2. You see Testman."
        self.assertEqual(expected, room.describe_room())

    def test_room_with_invisible_person(self):
        room = Test_Objects.TEST_ROOM_WITH_INVISIBLE_PERSON
        expected = "Test Room With Invis Person\nThis is a test room for testing people. You see a test 2."
        self.assertEqual(expected, room.describe_room())
