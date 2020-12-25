import Constants


class Room:

    # Name: Name of the room.
    # Desc: What the player sees when entering the room or looking in the room.
    # Exits: Dictionary of {direction: Room} indicating valid exits to this room.
    # Items: List of Item objects indicating items present in this room.

    def __init__(self, name, desc, exits, items):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.items = items

    # Describe the room plus all visible items in it.
    def describe_room(self):
        description = self.desc
        for item in self.items:
            if item.get_is_visible():
                description += " "
                description += get_item_seen_string(item)
                description += item.get_name()
                description += "."
        return description

    # When entering a room, describe the room and all items in it. No other functionality yet, but more readable.
    def enter_room(self):
        return self.describe_room()

    # If the direction the player wants to move is valid, move the player and describe the new room.
    # Otherwise, tell the player they can't do that.
    def exit_room(self, player, direction):
        if direction in self.exits:
            player.location = self.exits[direction]
            return self.exits[direction].enter_room()
        else:
            return Constants.EXIT_NOT_FOUND_STRING

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)


# Shows the grammatically correct syntax. "You see a ball". "You see an ice-cream".
def get_item_seen_string(item):
    if item.get_name()[0] in "aeiou":
        return Constants.YOU_SEE_AN_ITEM_STRING
    return Constants.YOU_SEE_A_ITEM_STRING
