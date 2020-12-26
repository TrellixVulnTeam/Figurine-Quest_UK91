import unittest
from game import Constants
from test import Objects


class TestItem(unittest.TestCase):

    def test_item_data(self):
        item = Objects.TEST_ITEM_IN_INVENTORY
        self.assertEqual(item.name, "test")
        self.assertEqual(item.short_desc, "Short desc")
        self.assertEqual(item.long_desc, "Long desc")
        self.assertEqual(item.is_visible, True)
        self.assertEqual(item.is_takeable, True)

    def test_take_item(self):
        room = Objects.TEST_ROOM
        player = Objects.TEST_PLAYER
        item = Objects.TEST_ITEM_ON_GROUND

        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)

        actual = item.take(player)

        self.assertTrue(item in player.inventory)
        self.assertTrue(item not in room.items)
        expected = Constants.ITEM_TAKEN_STRING + item.name + '.'
        self.assertEqual(expected, actual)

    def test_take_item_not_present(self):
        room = Objects.TEST_ROOM
        player = Objects.TEST_PLAYER
        item = Objects.TEST_ITEM_NOT_PRESENT

        self.assertTrue(item not in player.inventory)
        self.assertTrue(item not in room.items)

        actual = item.take(player)
        self.assertTrue(item not in player.inventory)
        self.assertTrue(item not in room.items)
        expected = Constants.ITEM_NOT_VISIBLE_STRING + item.name + '.'
        self.assertEqual(expected, actual)

    def test_take_invisible_item(self):
        room = Objects.TEST_ROOM_2
        player = Objects.TEST_PLAYER
        item = Objects.TEST_ITEM_NO_VIS

        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)

        actual = item.take(player)
        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)
        expected = Constants.ITEM_NOT_VISIBLE_STRING + item.name + '.'
        self.assertEqual(expected, actual)

    def test_take_untakeable_item(self):
        room = Objects.TEST_ROOM_2
        player = Objects.TEST_PLAYER_2
        item = Objects.TEST_ITEM_NO_GET

        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)

        actual = item.take(player)
        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)
        expected = Constants.ITEM_NOT_TAKEABLE_STRING + item.name + '.'
        self.assertEqual(expected, actual)
