import unittest
import Constants


class TestItem(unittest.TestCase):

    def test_item_data(self):
        item = Constants.TEST_ITEM_IN_INVENTORY
        self.assertEqual(item.name, "test")
        self.assertEqual(item.short_desc, "Short desc")
        self.assertEqual(item.long_desc, "Long desc")
        self.assertEqual(item.is_visible, True)
        self.assertEqual(item.is_takeable, True)

    def test_take_item(self):
        room = Constants.TEST_ROOM
        player = Constants.TEST_PLAYER
        item = Constants.TEST_ITEM_ON_GROUND

        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)

        actual = item.takeItem(player)

        self.assertTrue(item in player.inventory)
        self.assertTrue(item not in room.items)
        expected = Constants.ITEM_TAKEN_STRING + item.name + '.'
        self.assertEqual(expected, actual)

    def test_take_item_not_present(self):
        room = Constants.TEST_ROOM
        player = Constants.TEST_PLAYER
        item = Constants.TEST_ITEM_NOT_PRESENT

        self.assertTrue(item not in player.inventory)
        self.assertTrue(item not in room.items)

        actual = item.takeItem(player)
        self.assertTrue(item not in player.inventory)
        self.assertTrue(item not in room.items)
        expected = Constants.ITEM_NOT_VISIBLE_STRING + item.name + '.'
        self.assertEqual(expected, actual)

    def test_take_invisible_item(self):
        room = Constants.TEST_ROOM_2
        player = Constants.TEST_PLAYER
        item = Constants.TEST_ITEM_NO_VIS

        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)

        actual = item.takeItem(player)
        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)
        expected = Constants.ITEM_NOT_VISIBLE_STRING + item.name + '.'
        self.assertEqual(expected, actual)

    def test_take_untakeable_item(self):
        room = Constants.TEST_ROOM_2
        player = Constants.TEST_PLAYER_2
        item = Constants.TEST_ITEM_NO_GET

        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)

        actual = item.takeItem(player)
        self.assertTrue(item not in player.inventory)
        self.assertTrue(item in room.items)
        expected = Constants.ITEM_NOT_TAKEABLE_STRING + item.name + '.'
        self.assertEqual(expected, actual)
