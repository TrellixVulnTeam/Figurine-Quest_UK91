from game import Person, Constants
from game.content import Dialogue


# Molly is one of the two cats in the game. She's currently in the shed with the bear figurine.
class Molly(Person.Person):

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            return Dialogue.MOLLY_TALK_DIALOGUE
        return Constants.PERSON_NOT_VISIBLE_STRING
