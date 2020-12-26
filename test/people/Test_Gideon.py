import unittest
from test import Objects
from game.content import Dialogue
from game import Constants


class TestGideon(unittest.TestCase):
    def test_talk_gideon_present_and_visible(self):
        player = Objects.TEST_PLAYER_IN_GIDEON_ROOM
        gideon = Objects.TEST_GIDEON
        actual = gideon.talk(player)
        self.assertEqual(Dialogue.GIDEON_TALK_DIALOGUE, actual)

    def test_talk_gideon_invisible(self):
        player = Objects.TEST_PLAYER_IN_GIDEON_ROOM
        gideon = Objects.TEST_INVISIBLE_GIDEON
        actual = gideon.talk(player)
        self.assertEqual(Constants.PERSON_NOT_VISIBLE_STRING, actual)

    def test_talk_gideon_not_present(self):
        player = Objects.TEST_PLAYER
        gideon = Objects.TEST_GIDEON
        actual = gideon.talk(player)
        self.assertEqual(Constants.PERSON_NOT_VISIBLE_STRING, actual)
