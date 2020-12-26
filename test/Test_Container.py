import unittest

from game import Container, Player, Room, Constants
from test import Objects


class TestContainer(unittest.TestCase):
    def test_empty_container(self):
        container = Container.Container("test", ["keyword"], "Short desc", "Long desc", True, False, [])
        room = Room.Room("Test Room", "desc", {}, [container], [])
        player = Player.Player(room, [])
        actual = container.examine(player)
        expected = container.long_desc
        self.assertEqual(expected, actual)

    def test_container_with_item(self):
        container = Container.Container("test", ["keyword"], "Short desc", "Long desc",
                                        True, False, [Objects.TEST_ITEM_ON_GROUND])
        room = Room.Room("Test Room", "desc", {}, [container], [])
        player = Player.Player(room, [])
        self.assertEqual(container.contains, [Objects.TEST_ITEM_ON_GROUND])
        self.assertEqual(room.items, [container])

        actual = container.examine(player)
        expected = container.long_desc + '. ' + Constants.ITEM_REMOVED_FROM_CONTAINER_STRING +\
                   Objects.TEST_ITEM_ON_GROUND.name + '.'
        self.assertEqual(expected, actual)
        self.assertEqual(container.contains, [])
        self.assertEqual(room.items, [container, Objects.TEST_ITEM_ON_GROUND])
