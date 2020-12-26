from game import Person, Constants
from game.content import Dialogue


# Azuri is one of the two cats in the game. She's shy, but has one of the figurines hidden under Mum's bed.
class Azuri(Person.Person):
    spoken_to = False

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            if not self.spoken_to:
                # Reveal the figurine from Azuri.
                player.location.items[0].is_visible = True
                player.location.items[0].is_gettable = True
                return Dialogue.AZURI_FIRST_TALK_DIALOGUE
            return Dialogue.AZURI_SECOND_TALK_DIALOGUE
        return Constants.PERSON_NOT_VISIBLE_STRING
