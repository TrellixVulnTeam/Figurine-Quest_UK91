from game import Person, Constants
from game.content import Dialogue, Items


# Gideon is a cute 3-year-old who has found one of the figures the player wants. He asks for chocolate in exchange.
# He is the protagonist's grandson.
class Gideon(Person.Person):
    quest_complete = False

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            if not self.quest_complete:
                return Dialogue.GIDEON_TALK_DIALOGUE
            return Dialogue.GIDEON_POST_QUEST_DIALOGUE
        return Constants.PERSON_NOT_VISIBLE_STRING

    def give(self, item, player):
        if item is Items.CHOCOLATE:
            player.inventory.remove(Items.CHOCOLATE)
            Items.DOG_FIGURINE.is_visible = True
            Items.DOG_FIGURINE.is_takeable = True
            return Dialogue.GIDEON_QUEST_COMPLETE_DIALOGUE
        return Constants.INCORRECT_GIFT
