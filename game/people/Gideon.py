from game import Person, Constants
from game.content import Dialogue


class Gideon(Person.Person):

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            return Dialogue.GIDEON_TALK_DIALOGUE
        return Constants.PERSON_NOT_VISIBLE_STRING
