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

    # When entering a room, describe the room and all items in it.
    def enter_room(self):
        description = self.desc
        for item in self.items:
            if item.get_is_visible():
                description += " "
                description += get_item_seen_string(item)
                description += item.get_name()

    def exitRoom(self, player, direction):
        if direction in self.exits:
            player.location = self.exits[direction]
            self.exits[direction].enter_room()


# Shows the grammatically correct syntax. "You see a ball". "You see an ice-cream".
def get_item_seen_string(item):
    if item.get_name()[0] in "aeiou":
        return Constants.YOU_SEE_AN_ITEM_STRING
    return Constants.YOU_SEE_A_ITEM_STRING
