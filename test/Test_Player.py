import unittest

import Constants


class TestPlayer(unittest.TestCase):
    def test_inventory(self):
        player = Constants.TEST_PLAYER
        print(player.get_inventory())
        self.assertEqual("You have: \ntest", player.get_inventory())


if __name__ == '__main__':
    unittest.main()
