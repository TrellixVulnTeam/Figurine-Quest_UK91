# Start
WELCOME_MESSAGE = "Welcome to Figurine Quest! \n" \
                   "You'll be playing as Melody in this game, doing a task for your mother, once you find her. \n" \
                   "This is a text game. To interact with the game, type a command below. \n" \
                   "If you are unsure what commands are available, type 'help'. \n" \
                   "Good luck!"

# Quit
YES = ["y", "yes"]

# Victory
YOU_WIN_MESSAGE = "Congratulations. You win! You collected all five figurines. Hope you enjoyed playing!"

# Item
ITEM_NOT_VISIBLE_STRING = "You don't see the "
ITEM_NOT_TAKEABLE_STRING = "You can't reach the "
ITEM_TAKEN_STRING = "You took the "
YOU_SEE_AN_ITEM_STRING = "You see an "
YOU_SEE_A_ITEM_STRING = "You see a "
ITEM_NOT_IN_INVENTORY_STRING = "You don't have the "
ITEM_REMOVED_FROM_CONTAINER_STRING = "You remove the "
EMPTY_INVENTORY_STRING = "Nothing."

# Person
PERSON_VISIBLE_STRING = "You see "
PERSON_NOT_VISIBLE_STRING = "You don't see "
BASE_DIALOGUE = "They don't feel like talking right now."
INCORRECT_GIFT = "They don't want that item."

# Room
EXIT_NOT_FOUND_STRING = "You can't go that way."

# Player
INVENTORY_START_STRING = "You have: "

# Commands
DIRECTIONS = [["n", "e", "s", "w", "north", "east", "south", "west"]]

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

PLAYER_HELP = "This is a text game. To do things, read the description of the place you " \
              "are in, decide on your move, and type a command into the window. Here are your available commands: \n" \
              "n, e, s, w: Go North, East, South, or West. Read the room description to see available exits. \n" \
              "help: Read this help section again. \n" \
              "look: Look around the area. Shows the room's description again. \n" \
              "examine <object>: Examine an object more closely. To look at a ball, type \"examine ball\". \n" \
              "get <object>: Get an object. The object must be in the room and accessible to you. \n" \
              "talk <person>: Talk to a person. The person must be in the room. \n" \
              "give <object> <person>: Give someone an item. To give Jay the ball, you would type \"give ball jay\"" \
              "\n\n Good luck! If you run into trouble, remember to read carefully and 'examine' things closely!"
