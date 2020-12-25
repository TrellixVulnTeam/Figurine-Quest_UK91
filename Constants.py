import Item
import Room
import Player

# Quit
YES = ["y", "yes"]

# Item
PLAYER_HAS_ITEM_STRING = "You already have that!"
ITEM_NOT_VISIBLE_STRING = "You don't see that here."
ITEM_NOT_TAKEABLE_STRING = "You can't reach that yet."
ITEM_TAKEN_PREFIX_STRING = "You took the "
YOU_SEE_AN_ITEM_STRING = "You see an "
YOU_SEE_A_ITEM_STRING = "You see a "

# Room
EXIT_NOT_FOUND_STRING = "You can't go that way."

# Player
INVENTORY_START_STRING = "You have: "

# Test Objects
TEST_ITEM_IN_INVENTORY = Item.Item("test", "Short desc", "Long desc", True, True)
TEST_ITEM_ON_GROUND = Item.Item("test 2", "Short desc 2", "Long desc 2", True, True)
TEST_ITEM_NOT_PRESENT = Item.Item("test not present", "Short desc not present", "Long desc not present", True, True)
TEST_ITEM_NO_GET = Item.Item("test UnGettable", "Short desc ungettable", "Long desc ungettable", True, False)
TEST_ITEM_NO_VIS = Item.Item("test Invisible", "Short desc invisible", "Long desc invisible", False, True)
TEST_ROOM = Room.Room("Test Room", "This is a test room for testing.", {}, [TEST_ITEM_ON_GROUND])
TEST_ROOM_2 = Room.Room("Test Room 2", "This is a test room 2 for testing.", {"s": TEST_ROOM},
                        [TEST_ITEM_ON_GROUND, TEST_ITEM_NO_GET, TEST_ITEM_NO_VIS])
TEST_ROOM.exits = {"n": TEST_ROOM_2}
TEST_PLAYER = Player.Player(TEST_ROOM, [TEST_ITEM_IN_INVENTORY])
TEST_PLAYER_2 = Player.Player(TEST_ROOM_2, [TEST_ITEM_IN_INVENTORY])

# Commands
DIRECTIONS = ["n", "e", "s", "w", "north", "east", "south", "west"]

HELP = ["h", "help", "hint"]
INVENTORY = ["i", "inv", "inventory"]
LOOK = ["l", "look"]
QUIT = ["q", "quit", "exit", "stop"]

EXAMINE = ["ex", "examine"]
GIVE = ["give"]
TAKE = ["get", "take"]
TALK = ["talk", "ask"]

UNTARGETABLE_COMMANDS = [HELP, INVENTORY, LOOK, QUIT]
SINGLE_TARGET_COMMANDS = [EXAMINE, TAKE, TALK]
DOUBLE_TARGET_COMMANDS = [GIVE]
VALID_COMMANDS = DIRECTIONS + UNTARGETABLE_COMMANDS + SINGLE_TARGET_COMMANDS + DOUBLE_TARGET_COMMANDS
INVALID_COMMAND_GIVEN_STRING = "That is not a valid command. For a list of commands, type \'help\'"
IMPROPERLY_PARSED_COMMAND = "This command was passed to a place in the program it shouldn't go. " \
                            "Please tell Jay about it."

PLAYER_HELP = "This is a text game. To do things, read the description of the place you" \
              "are in, decide on your move, and type a command into the window. Here are your available commands: \n" \
              "n, e, s, w: Go North, East, South, or West. Read the room description to see available exits. \n" \
              "help: Read this help section again. \n" \
              "look: Look around the area. Shows the room's description again. \n" \
              "examine <object>: Examine an object more closely. To look at a ball, type \"examine ball\". \n" \
              "get <object>: Get an object. The object must be in the room and accessible to you. \n" \
              "talk <person>: Talk to a person. The person must be in the room. \n" \
              "give <object> <person>: Give someone an item. To give Jay the ball, you would type \"give ball jay\"" \
              "\n\n Good luck! If you run into trouble, remember to read carefully and 'examine' things closely!"
