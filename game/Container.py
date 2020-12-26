from game import Item, Constants

# A container is an item that holds other items. When examined, the container reveals the new items.
# TODO: Require 'open' instead of 'examine'?
class Container(Item.Item):

    # Contains: A list of Item objects contained in the container.
    def __init__(self, name, keywords, short_desc, long_desc, is_visible, is_takeable, contains):
        self.name = name
        self.keywords = keywords
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.is_visible = is_visible
        self.is_takeable = is_takeable
        self.contains = contains

    def examine(self, player):
        room = player.location
        if not self.is_visible:
            return Constants.ITEM_NOT_VISIBLE_STRING + self.name + '.'
        if self not in room.items and self not in player.inventory:
            return Constants.ITEM_NOT_VISIBLE_STRING + self.name + '.'

        description = self.long_desc
        if len(self.contains) > 0:
            description += '. '

        # TODO: Add code for invisible items?
        for item in self.contains:
            description += Constants.ITEM_REMOVED_FROM_CONTAINER_STRING + item.name + '.'
            item.is_visible = True
            self.contains.remove(item)
            room.items.append(item)
        return description
