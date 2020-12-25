import Item
import Room
import Player


# Item
PLAYER_HAS_ITEM_STRING = "You already have that!"
ITEM_NOT_VISIBLE_STRING = "You don't see that here."
ITEM_NOT_TAKEABLE_STRING = "You can't reach that yet."
ITEM_TAKEN_PREFIX_STRING = "You took the "
YOU_SEE_AN_ITEM_STRING = "You see an "
YOU_SEE_A_ITEM_STRING = "You see a "

# Room
EXIT_NOT_FOUND_STRING = "You can't move in that direction."

# Player
INVENTORY_START_STRING = "You have: "

# Test Objects
TEST_ITEM_IN_INVENTORY = Item.Item("test", "Short desc", "Long desc", True, True)
TEST_ITEM_ON_GROUND = Item.Item("test 2", "Short desc 2", "Long desc 2", True, True)
TEST_ITEM_NOT_PRESENT = Item.Item("test not present", "Short desc not present", "Long desc not present", True, True)
TEST_ITEM_NO_GET = Item.Item("test UnGettable", "Short desc ungettable", "Long desc ungettable", True, False)
TEST_ITEM_NO_VIS = Item.Item("test Invisible", "Short desc invisible", "Long desc invisible", False, True)
TEST_ROOM = Room.Room("Test Room", "This is a test room for testing.", {"n": "Test Room 2"}, [TEST_ITEM_ON_GROUND])
TEST_ROOM_2 = Room.Room("Test Room 2", "This is a test room 2 for testing.", {"s": "Test Room"},
                        [TEST_ITEM_ON_GROUND, TEST_ITEM_NO_GET, TEST_ITEM_NO_VIS])
TEST_PLAYER = Player.Player(TEST_ROOM, [TEST_ITEM_IN_INVENTORY])
TEST_PLAYER_2 = Player.Player(TEST_ROOM_2, [TEST_ITEM_IN_INVENTORY])
