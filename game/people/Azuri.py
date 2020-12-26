from game import Person, Constants
from game.content import Dialogue


# Azuri is one of the two cats in the game. She's shy, but has one of the figurines hidden under Mum's bed.
class Azuri(Person.Person):

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            return Dialogue.AZURI_FIRST_TALK_DIALOGUE
        return Constants.PERSON_NOT_VISIBLE_STRING
