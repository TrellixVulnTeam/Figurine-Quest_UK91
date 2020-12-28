import unittest

from game import Constants
from game.content import Test_Objects


class TestPerson(unittest.TestCase):
    def test_visible_person(self):
        person = Test_Objects.TEST_PERSON
        player = Test_Objects.TEST_PLAYER_IN_PERSON_ROOM
        actual = person.examine(player)
        self.assertEqual(person.desc, actual)

    def test_invisible_person(self):
        person = Test_Objects.TEST_INVISIBLE_PERSON
        player = Test_Objects.TEST_PLAYER_IN_PERSON_ROOM
        actual = person.examine(player)
        self.assertEqual(Constants.PERSON_NOT_VISIBLE_STRING, actual)

    def test_person_not_present(self):
        person = Test_Objects.TEST_PERSON
        player = Test_Objects.TEST_PLAYER
        actual = person.examine(player)
        self.assertEqual(Constants.PERSON_NOT_VISIBLE_STRING, actual)

