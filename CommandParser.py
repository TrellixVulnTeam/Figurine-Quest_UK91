import Commands
import Constants


# Contains functions for parsing user commands into actions.
def get_input():
    return input()


def parse_input(user_input, player):
    user_input = user_input.lower()
    if not is_command_valid(user_input, Constants.VALID_COMMANDS):
        return Constants.INVALID_COMMAND_GIVEN_STRING
    if user_input in Constants.UNTARGETABLE_COMMANDS:
        parse_untargetable_command(user_input, player)
    else:
        parse_targetable_command(user_input, player)


# Handles single-word commands with no target.
def parse_untargetable_command(user_input, player):
    if user_input in Constants.DIRECTIONS:
        return Commands.parse_move_command(user_input, player)
    if user_input in Constants.HELP:
        return Commands.parse_help_command()
    if user_input in Constants.LOOK:
        return Commands.parse_look_command(player)
    if user_input in Constants.QUIT:
        return Commands.parse_quit_command()
    return Constants.IMPROPERLY_PARSED_COMMAND


# Parse a command with one or more targets, like "examine ball", or "give ball jay".
def parse_targetable_command(user_input, player):
    user_input = user_input.split()
    command = user_input[0]

    if len(user_input) < 2 or len(user_input) > 3:
        return Constants.IMPROPERLY_PARSED_COMMAND

    if len(user_input) == 2:
        if is_command_valid(command, Constants.SINGLE_TARGET_COMMANDS):
            return parse_single_target_command(user_input, player)
    if len(user_input) == 3:
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
    for command_list in allowable_commands:
        for command in command_list:
            if user_input == command:
                return True
    return False
