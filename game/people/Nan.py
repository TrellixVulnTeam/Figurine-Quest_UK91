from game import Person, Constants
from game.content import Dialogue, Items


# Nan is an older lady in her 60's. She gives the main quest for the game, finding her five figurines.
class Nan(Person.Person):

    figurines_found = 0
    spoken_to = False
    figurines_wanted = [Items.DOG_FIGURINE, Items.CAT_FIGURINE, Items.MOUSE_FIGURINE, Items.BEAR_FIGURINE,
                        Items.PIG_FIGURINE]

    def talk(self, player):
        if self in player.location.people and self.is_visible:
            if not self.spoken_to:
                self.spoken_to = True
                return Dialogue.NAN_INITIAL_TALK_DIALOGUE
            if self.figurines_found < 5:
                # Tells the user how many figurines they've given Nan and how many are still needed.
                return Dialogue.NAN_SUBSEQUENT_DIALOGUE_1 + str(self.figurines_found) + \
                       Dialogue.NAN_SUBSEQUENT_DIALOGUE_2 + str(len(self.figurines_wanted)) + \
                       Dialogue.NAN_SUBSEQUENT_DIALOGUE_3
        return Constants.PERSON_NOT_VISIBLE_STRING

    # If the item is a figurine, take the figurine and remove it from the list of wanted items.
    # If the wanted items list is empty, the player wins.
    def give(self, item, player):
        if self in player.location.people and self.is_visible:
            if item in self.figurines_wanted:
                player.remove_item(item)
                self.figurines_wanted.remove(item)
                self.figurines_found += 1
                if len(self.figurines_wanted) == 0:
                    return Dialogue.NAN_VICTORY_DIALOGUE
                    # TODO: Add victory code here.
                return Dialogue.NAN_SUBSEQUENT_DIALOGUE_1 + str(self.figurines_found) + \
                       Dialogue.NAN_SUBSEQUENT_DIALOGUE_2 + str(len(self.figurines_wanted)) + \
                       Dialogue.NAN_SUBSEQUENT_DIALOGUE_3
            return Constants.INCORRECT_GIFT
        return Constants.PERSON_NOT_VISIBLE_STRING
