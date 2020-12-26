from game import Constants


# Completes commands after the parser has determined which function to call.

# Untargetable commands

# Move the player in a direction if valid.
def parse_move_command(user_input, player):
    return player.move_room(user_input[0][0])


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


def parse_inventory_command(player):
    return player.get_inventory()


# Single target commands

# Returns long description of an item if it is present in the room or player's inventory.
def parse_examine_command(user_input, player):
    target = joinList(user_input[1:])
    for item in player.location.items:
        if target == item.name.lower() or target in item.keywords:
            return item.examine(player)
    for item in player.inventory:
        if target == item.name.lower():
            return item.examine(player)
    return Constants.ITEM_NOT_VISIBLE_STRING + target + '.'


# Gets the item if it is present in the room.
def parse_take_command(user_input, player):
    target = joinList(user_input[1:])
    for item in player.location.items:
        if target == item.name.lower() or target in item.keywords:
            return item.take(player)
    return Constants.ITEM_NOT_VISIBLE_STRING + target + '.'


# Talks to an NPC and gets dialogue in return.
def parse_talk_command(user_input, player):
    target = joinList(user_input[1:])
    for person in player.location.people:
        if target == person.name.lower():
            return person.talk(player)
    return Constants.PERSON_NOT_VISIBLE_STRING + target + '.'


# Double target commands

# Tries to give an item to an NPC.
def parse_give_command(user_input, player):
    target = user_input[1]
    item_name = joinList(user_input[2:])
    item = None

    # TODO: Dehack this?
    for inv_item in player.inventory:
        if inv_item.name == item_name or item_name in inv_item.keywords:
            item = inv_item

    if item is None:
        return Constants.ITEM_NOT_IN_INVENTORY_STRING + item_name + '.'

    for person in player.location.people:
        if target == person.name.lower():
            return person.give(item, player)
    return Constants.PERSON_NOT_VISIBLE_STRING + target + '.'


def joinList(input_list):
    separator = ' '
    return separator.join(input_list)
