from game import Commands, Constants


# Takes in user input from the player and determines where to send it for parsing.
# Input is divided into commands with targets like 'get <item>', and items without
# targets, like 'help' or 'look'.
def parse_input(user_input, player):
    user_input = user_input.lower().split()
    if len(user_input) == 0:  # Empty strings are always invalid commands.
        return Constants.INVALID_COMMAND_GIVEN_STRING

    # Check to see if the first word is a proper command.
    if not is_command_valid(user_input[0], Constants.VALID_COMMANDS):
        return Constants.INVALID_COMMAND_GIVEN_STRING

    # If a command is one word, it shouldn't have a target.
    if len(user_input) == 1:
        return parse_untargetable_command(user_input, player)

    return parse_targetable_command(user_input, player)


# Handles single-word commands with no target, such as 'help' or 'inventory'.
def parse_untargetable_command(user_input, player):
    command = user_input[0]
    if command in Constants.DIRECTIONS[0]:
        return Commands.parse_move_command(user_input, player)
    if command in Constants.HELP:
        return Commands.parse_help_command()
    if command in Constants.LOOK:
        return Commands.parse_look_command(player)
    if command in Constants.QUIT:
        return Commands.parse_quit_command()
    if command in Constants.INVENTORY:
        return Commands.parse_inventory_command(player)

    # If the command is in the targeted commands like 'examine' or 'give', tell the player this.
    if is_command_valid(user_input, Constants.SINGLE_TARGET_COMMANDS +
                                    Constants.DOUBLE_TARGET_COMMANDS):
        return Constants.IMPROPERLY_TARGETED_COMMAND

    return Constants.INVALID_COMMAND_GIVEN_STRING


# Parse a command with one or more targets, like "examine ball", or "give ball jay".
def parse_targetable_command(user_input, player):
    command = user_input[0]

    # This should not occur - one-word commands should always go to parse_untargetable_command.
    if len(user_input) < 2:
        return Constants.IMPROPERLY_PARSED_COMMAND

    # Parse a command with only one target, like 'get <item>'
    if is_command_valid(command, Constants.SINGLE_TARGET_COMMANDS):
        return parse_single_target_command(user_input, player)

    # Parse a command with two targets, like 'give <person> <item>'.
    if is_command_valid(command, Constants.DOUBLE_TARGET_COMMANDS):
        return parse_double_target_command(user_input, player)

    return Constants.INVALID_COMMAND_GIVEN_STRING


def parse_single_target_command(user_input, player):
    command = user_input[0]
    if command in Constants.EXAMINE:
        return Commands.parse_examine_command(user_input, player)
    if command in Constants.TAKE:
        return Commands.parse_take_command(user_input, player)
    if command in Constants.TALK:
        return Commands.parse_talk_command(user_input, player)
    return Constants.INVALID_COMMAND_GIVEN_STRING


def parse_double_target_command(user_input, player):
    command = user_input[0]
    if command in Constants.GIVE:
        return Commands.parse_give_command(user_input, player)
    return Constants.INVALID_COMMAND_GIVEN_STRING


# Searches all valid commands. Returns True if the user command is present, else returns False.
def is_command_valid(user_input, allowable_commands):
    # Flatten the list of allowable commands, since many allowable commands are a list
    # of allowable commands, like ['h', 'help', 'hint'] that return the same command.
    flat_allowable_commands = []
    for sublist in allowable_commands:
        for item in sublist:
            flat_allowable_commands.append(item)

    for command in flat_allowable_commands:
        if command in [user_input, user_input[0]]:  # TODO: Fix hack?
            return True
    return False
