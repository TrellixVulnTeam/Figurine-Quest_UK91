from game import Constants


class Person:

    def __init__(self, name, desc, is_visible):
        self.name = name
        self.desc = desc
        self.is_visible = is_visible

    def examine(self, player):
        if self in player.location.people and self.is_visible:
            return self.desc
        return Constants.PERSON_NOT_VISIBLE_STRING
