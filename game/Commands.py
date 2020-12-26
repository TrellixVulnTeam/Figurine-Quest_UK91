from game import Constants


# Completes commands after the parser has determined which function to call.

# Untargetable commands

# Move the player in a direction if valid.
def parse_move_command(user_input, player):
    return player.move_room(user_input[0])


# Display the help text on the screen.
def parse_help_command():
    return Constants.PLAYER_HELP


# Confirm the player wants to quit.
def parse_quit_command():
    print("Are you sure you want to quit? Yes/No")
    user_input = input()
    if user_input.lower() in Constants.YES:
        print("Thank you for playing!")
        exit()
    return "Okay."


# Display the room description.
def parse_look_command(player):
    return player.location.desc


# Single target commands

# Returns long description of an item if it is present in the room or player's inventory.
def parse_examine_command(user_input, player):
    target = user_input[1:]
    separator = ' '
    target = separator.join(target)
    for item in player.location.items:
        if target == item.name:
            return item.long_desc
    for item in player.inventory:
        if target == item.name:
            return item.long_desc
    return Constants.ITEM_NOT_VISIBLE_STRING + target + '.'


# Gets the item if it is present in the room.
def parse_take_command(user_input, player):
    target = user_input[1:]
    separator = ' '
    target = separator.join(target)
    for item in player.location.items:
        if target == item.name:
            return item.takeItem(player)
    return Constants.ITEM_NOT_VISIBLE_STRING + target + '.'


def parse_talk_command(user_input, player):
    return "To be implemented when NPC's are implemented."


# Double target commands

def parse_give_command(user_input, player):
    return "To be implemented when NPC's are implemented."
