from game import Person, Constants
from game.content import Dialogue


# Gideon is a cute 3-year-old who has found one of the figures the player wants. He asks for chocolate in exchange.
# He is the protagonist's grandson.
class Gideon(Person.Person):

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            return Dialogue.GIDEON_TALK_DIALOGUE
        return Constants.PERSON_NOT_VISIBLE_STRING
