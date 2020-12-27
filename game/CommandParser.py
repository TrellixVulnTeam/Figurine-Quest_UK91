from game import Commands, Constants


# Contains functions for parsing user commands into actions.
def get_input():
    return input()


def parse_input(user_input, player):
    user_input = user_input.lower().split()
    if len(user_input) == 0:
        return Constants.INVALID_COMMAND_GIVEN_STRING
    if not is_command_valid(user_input[0], Constants.VALID_COMMANDS):
        return Constants.INVALID_COMMAND_GIVEN_STRING
    if len(user_input) == 1:
        return parse_untargetable_command(user_input, player)
    else:
        return parse_targetable_command(user_input, player)


# Handles single-word commands with no target.
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
    if is_command_valid(user_input, Constants.SINGLE_TARGET_COMMANDS + Constants.DOUBLE_TARGET_COMMANDS):
        return Constants.IMPROPERLY_TARGETED_COMMAND
    return Constants.IMPROPERLY_PARSED_COMMAND


# Parse a command with one or more targets, like "examine ball", or "give ball jay".
def parse_targetable_command(user_input, player):
    command = user_input[0]

    if len(user_input) < 2:
        return Constants.IMPROPERLY_PARSED_COMMAND

    if is_command_valid(command, Constants.SINGLE_TARGET_COMMANDS):
        return parse_single_target_command(user_input, player)

    if is_command_valid(command, Constants.DOUBLE_TARGET_COMMANDS):
        return parse_double_target_command(user_input, player)

    return Constants.IMPROPERLY_PARSED_COMMAND


def parse_single_target_command(user_input, player):
    command = user_input[0]
    if command in Constants.EXAMINE:
        return Commands.parse_examine_command(user_input, player)
    if command in Constants.TAKE:
        return Commands.parse_take_command(user_input, player)
    if command in Constants.TALK:
        return Commands.parse_talk_command(user_input, player)
    return Constants.IMPROPERLY_PARSED_COMMAND


def parse_double_target_command(user_input, player):
    command = user_input[0]
    if command in Constants.GIVE:
        return Commands.parse_give_command(user_input, player)
    return Constants.IMPROPERLY_PARSED_COMMAND


# Searches all valid commands. Returns True if the user command is in there, otherwise returns False.
def is_command_valid(user_input, allowable_commands):
    # Flatten the list of allowable commands, since many allowable commands are a list of synonyms. ['get', 'take']
    flat_allowable_commands = []
    for sublist in allowable_commands:
        for item in sublist:
            flat_allowable_commands.append(item)

    for command in flat_allowable_commands:
        if user_input == command or user_input[0] == command:  # TODO: Fix hack
            return True
    return False
