from game import Person
from game.content import Dialogue


class Gideon(Person.Person):

    def talk(self, player):
        if self.name in player.location.people and self.is_visible:
            return Dialogue.GIDEON_DIALOGUE
