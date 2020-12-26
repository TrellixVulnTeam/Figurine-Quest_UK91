from game import Person, Constants
from game.content import Dialogue


# Jay is 29 years old and a software developer. He programmed this game and doesn't hesitate to break the fourth
# wall as a result. He's the protagonist's son.
class Jay(Person.Person):

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            return Dialogue.JAY_TALK_DIALOGUE
        return Constants.PERSON_NOT_VISIBLE_STRING
