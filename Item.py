import Constants


class Item:

    # short_desc - what the player sees when looking at inventory or a room with the item.
    # long_desc - What the player sees when examining the item.
    # is_visible - Determines if the item can currently be seen.
    # is_takeable - Determines if the player can currently "take" the item.

    def __init__(self, name, short_desc, long_desc, is_visible, is_takeable):
        self.name = name
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.is_visible = is_visible
        self.is_takeable = is_takeable

    def get_name(self):
        return self.name

    def get_short_desc(self):
        return self.short_desc

    def get_long_desc(self):
        return self.long_desc

    def get_is_visible(self):
        return self.is_visible

    # Code for when the player tries to "get" or "take" an item.
    # Checks to see if the player has the item.
    # Checks to see if the item is inside the room and visible to the player.
    # Checks to see if the item can be taken.
    # If all conditions are met, removes item from room and adds to player's inventory.
    # Returns a message indicating what did or did not occur.
    def takeItem(self, player):
        if self in player.getItems():
            return Constants.PLAYER_HAS_ITEM_STRING
        room = player.getLocation()
        if self not in room.getItems() or not self.is_visible:
            return Constants.ITEM_NOT_VISIBLE_STRING
        if not self.is_takeable:
            return Constants.ITEM_NOT_TAKEABLE_STRING

        player.addItem(self)
        room.removeItem(self)
        return Constants.ITEM_TAKEN_PREFIX_STRING + self.name
