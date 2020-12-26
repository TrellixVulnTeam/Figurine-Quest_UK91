from game import Constants


class Item:

    # short_desc - what the player sees when looking at inventory or a room with the item.
    # long_desc - What the player sees when examining the item.
    # is_visible - Determines if the item can currently be seen.
    # is_takeable - Determines if the player can currently "take" the item.

    def __init__(self, name, keywords, short_desc, long_desc, is_visible, is_takeable):
        self.name = name
        self.keywords = keywords
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.is_visible = is_visible
        self.is_takeable = is_takeable

    # Code for when the player tries to "get" or "take" an item.
    # Checks to see if the player has the item.
    # Checks to see if the item is inside the room and visible to the player.
    # Checks to see if the item can be taken.
    # If all conditions are met, removes item from room and adds to player's inventory.
    # Returns a message indicating what did or did not occur.
    def take(self, player):
        room = player.location
        if self not in room.items or not self.is_visible:
            return Constants.ITEM_NOT_VISIBLE_STRING + self.name + '.'
        if not self.is_takeable:
            return Constants.ITEM_NOT_TAKEABLE_STRING + self.name + '.'

        player.add_item(self)
        room.remove_item(self)
        return Constants.ITEM_TAKEN_STRING + self.name + "."

    def examine(self, player):
        room = player.location
        if not self.is_visible:
            return Constants.ITEM_NOT_VISIBLE_STRING + self.name + '.'
        if self in room.items or self in player.inventory:
            return self.long_desc
        return Constants.ITEM_NOT_VISIBLE_STRING + self.name + '.'
