from game import Item, Person, Player, Room, Container
from game.people import Gideon

# Test Objects

# Items
TEST_ITEM_IN_INVENTORY = Item.Item("test", ["keyword"], "Short desc", "Long desc", True, True)
TEST_ITEM_ON_GROUND = Item.Item("test 2", ["keyword"], "Short desc 2", "Long desc 2", True, True)
TEST_ITEM_NOT_PRESENT = Item.Item("test not present", ["keyword"], "Short desc not present", "Long desc not present", True, True)
TEST_ITEM_NO_GET = Item.Item("test ungettable", ["keyword"], "Short desc ungettable", "Long desc ungettable", True, False)
TEST_ITEM_NO_VIS = Item.Item("test invisible", ["keyword"], "Short desc invisible", "Long desc invisible", False, True)

# Containers
TEST_EMPTY_CONTAINER = Container.Container("test", ["keyword"], "Short desc", "Long desc", True, False, [])
TEST_CONTAINER_WITH_ITEM = Container.Container("test", ["keyword"], "Short desc", "Long desc",
                                               True, False, [TEST_ITEM_ON_GROUND])
TEST_CONTAINER_WITH_INVISIBLE_ITEM = Container.Container("test", ["keyword"], "Short desc", "Long desc",
                                                         True, False, [TEST_ITEM_NO_VIS])

# People
TEST_PERSON = Person.Person("Testman", "You see a test man", True)
TEST_INVISIBLE_PERSON = Person.Person("Testman", "You shouldn't see this test man", False)
TEST_GIDEON = Gideon.Gideon("Gideon", "You see a Gideon", True)
TEST_INVISIBLE_GIDEON = Gideon.Gideon("Gideon", "You should not see this Gideon", False)

# Rooms
TEST_ROOM = Room.Room("Test Room", "This is a test room for testing.", {}, [TEST_ITEM_ON_GROUND], [])
TEST_ROOM_2 = Room.Room("Test Room 2", "This is a test room 2 for testing.", {"s": TEST_ROOM},
                        [TEST_ITEM_ON_GROUND, TEST_ITEM_NO_GET, TEST_ITEM_NO_VIS], [])
TEST_ROOM.exits = {"n": TEST_ROOM_2}
TEST_ROOM_WITH_PERSON = Room.Room("Test Room With Person", "This is a test room for testing people.",
                                  {"n": TEST_ROOM_2}, [TEST_ITEM_ON_GROUND], [TEST_PERSON])
TEST_ROOM_WITH_INVISIBLE_PERSON = Room.Room("Test Room With Invis Person", "This is a test room for testing people.",
                                            {"n": TEST_ROOM_2}, [TEST_ITEM_ON_GROUND], [TEST_INVISIBLE_PERSON])
TEST_ROOM_WITH_GIDEON = Room.Room("Test Room With Gideon", "This is a test room for testing Gideon.",
                                  {"n": TEST_ROOM_2}, [TEST_ITEM_ON_GROUND], [TEST_GIDEON])
TEST_ROOM_WITH_INVISIBLE_GIDEON = Room.Room("Test Room With Gideon", "This is a test room for testing Gideon.",
                                  {"n": TEST_ROOM_2}, [TEST_ITEM_ON_GROUND], [TEST_INVISIBLE_GIDEON])

# Players
TEST_PLAYER = Player.Player(TEST_ROOM, [TEST_ITEM_IN_INVENTORY])
TEST_PLAYER_2 = Player.Player(TEST_ROOM_2, [TEST_ITEM_IN_INVENTORY])
TEST_PLAYER_IN_PERSON_ROOM = Player.Player(TEST_ROOM_WITH_PERSON, [TEST_ITEM_IN_INVENTORY])
TEST_PLAYER_IN_INVISIBLE_PERSON_ROOM = Player.Player(TEST_ROOM_WITH_INVISIBLE_PERSON, [TEST_ITEM_IN_INVENTORY])
TEST_PLAYER_IN_GIDEON_ROOM = Player.Player(TEST_ROOM_WITH_GIDEON, [TEST_ITEM_IN_INVENTORY])