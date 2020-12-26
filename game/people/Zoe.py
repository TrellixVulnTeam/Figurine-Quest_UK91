from game import Person, Constants
from game.content import Dialogue


# Zoe is a 27-year-old with bright purple hair. She's the mother of Gideon and the protagonist's daughter.
class Zoe(Person.Person):

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            return Dialogue.ZOE_TALK_DIALOGUE
        return Constants.PERSON_NOT_VISIBLE_STRING
