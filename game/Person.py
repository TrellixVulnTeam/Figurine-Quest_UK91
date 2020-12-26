from game import Constants


class Person:

    def __init__(self, name, desc, is_visible):
        self.name = name
        self.desc = desc
        self.is_visible = is_visible

    # TODO: Remove need for lower()?
    def examine(self, player):
        if self in player.location.people and self.is_visible:
            return self.desc
        return Constants.PERSON_NOT_VISIBLE_STRING + self.name.lower() + "."

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            return Constants.BASE_DIALOGUE
        return Constants.PERSON_NOT_VISIBLE_STRING + self.name.lower() + "."

    def give(self, item, player):
        if item not in player.inventory:
            return Constants.ITEM_NOT_IN_INVENTORY_STRING + item.name + "."
        if self in player.location.people and self.is_visible:
            return Constants.INCORRECT_GIFT
        return Constants.PERSON_NOT_VISIBLE_STRING + self.name.lower() + "."
