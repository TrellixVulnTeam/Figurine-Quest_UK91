from game import Room
from game.content import Items, People

# TODO: Add code to generate exit descriptions?
FRONT_YARD_DESCRIPTION = "You are out on the front yard of your home. It is well kept, showcasing your mother's eye \n" \
                         "for gardening. You see exits to the west, north, and east."
SIDE_PATH_DESCRIPTION = "You are on the left path. You can see that a lot of work has been done to it over the last \n" \
                        "couple of years to keep it in the shade. That's how Nan keeps busy, after all. You see \n" \
                        "exits to the north and south."
ZOE_CAR_DESCRIPTION = "Near the street, you see Zoe's pink car. She must be visiting. You see exits to the west and \n" \
                      "north."
DRIVEWAY_DESCRIPTION = "You are in the driveway of your home. Your car is there. You can hear the faint sound of \n" \
                       "conversation from the garden. You see exits to the north, west, and south."
SHED_DESCRIPTION = "You are in the shed. Molly has taken to making it a home now, getting in through the roof. You \n" \
                   "see exits to the north and south."
BACK_GARDEN_DESCRIPTION = "You are in the back garden. The sound of conversation is now clear as you spy the two \n" \
                          "inhabitants of the garden, sitting on chairs and talking. You see exits to the west, \n" \
                          "south, and east."
BACK_VERANDAH_DESCRIPTION = "You are on the back verandah. You can see Nan and Zoe chatting in the back garden from \n" \
                            "here. You see exits to the north and east."
LAUNDRY_DESCRIPTION = "You are in the laundry. The washing machine isn't currently running, and it looks like you're \n" \
                      "caught up on laundry for the time being. You see exits to the west, east, and south."
BATHROOM_DESCRIPTION = "You are in the bathroom. Nobody's in here right now. You see an exit to the west."
KITCHEN_DESCRIPTION = "You are in the kitchen. There's a slight spill of brown liquid on the countertop. Gideon's \n" \
                      "been making his coffee. He must be somewhere nearby. You see an exit to the west."
GUEST_ROOM_DESCRIPTION = "You are in the guest room. Jay's been staying here for the last few days. You can see \n" \
                         "his clothes are on the bed, to avoid falling victim to the cats. You see exits to the \n" \
                         "north, east, and south."
MUM_ROOM_DESCRIPTION = "You are in your room. At least one of the cats should be around, but you don't see \n" \
                       "any right now. Maybe they're hiding somewhere? You see an exit to the south."
LOUNGE_ROOM_ENTRY_DESCRIPTION = "You are in the loungeroom after just entering the house. Sun streams in through the \n" \
                                "door, but the screen door is shut to keep the cats in. The room is a study in \n" \
                                "controlled chaos as various toys are scattered about the area. I wonder who could \n" \
                                "have done that? You see exits to the south, north, and east."
LOUNGE_ROOM_EAST_DESCRIPTION = "You are in the loungeroom to the right of the door, near your and Nan's room. You \n" \
                               "see exits to the west, north, east, and south."
FRONT_VERANDAH_ROOM_DESCRIPTION = "You are on the front verandah. A few of Gideon's cars are scattered about. You \n" \
                                  "generally pick up after him, so he must have been here recently. You see exits \n" \
                                  "to the north and south."
NAN_ROOM_DESCRIPTION = "You are in Nan's room. There's not much to see here. You see an exit to the north."
STUDY_ROOM_DESCRIPTION = "You are in the study. Various art and craft supplies cover the shelves. Fortunately, there \n" \
                         "are no key items here - the designer of this game isn't cruel enough to make you search \n" \
                         "all around this room! You see an exit to the west."

# Instantiate rooms first, then create exits. A room must be instantiated to be pointed to as an exit.
FRONT_YARD_ROOM = Room.Room("Front Yard", FRONT_YARD_DESCRIPTION, {}, [], [])
SIDE_PATH_ROOM = Room.Room("Side Path", SIDE_PATH_DESCRIPTION, {}, [], [])
ZOE_CAR_ROOM = Room.Room("Zoe's Car", ZOE_CAR_DESCRIPTION, {}, [], [])
DRIVEWAY_ROOM = Room.Room("Driveway", DRIVEWAY_DESCRIPTION, {}, [], [])
SHED_ROOM = Room.Room("Shed", SHED_DESCRIPTION, {}, [Items.BEAR_FIGURINE], [People.MOLLY])
BACK_GARDEN_ROOM = Room.Room("Back Garden", BACK_GARDEN_DESCRIPTION, {}, [], [People.NAN, People.ZOE])
BACK_VERANDAH_ROOM = Room.Room("Back Verandah", BACK_VERANDAH_DESCRIPTION, {}, [], [])
LAUNDRY_ROOM = Room.Room("Laundry Room", LAUNDRY_DESCRIPTION, {}, [], [])
BATHROOM = Room.Room("Bathroom", BATHROOM_DESCRIPTION, {}, [], [])
KITCHEN = Room.Room("Kitchen", KITCHEN_DESCRIPTION, {}, [Items.CHOCOLATE], [])
GUEST_ROOM = Room.Room("Guest Room", GUEST_ROOM_DESCRIPTION, {}, [], [People.JAY])
MUM_ROOM = Room.Room("Mum's Room", MUM_ROOM_DESCRIPTION, {}, [], [People.AZURI])
LOUNGE_ROOM_ENTRY = Room.Room("Lounge Room Entry", LOUNGE_ROOM_ENTRY_DESCRIPTION, {}, [], [])
LOUNGE_ROOM_EAST = Room.Room("Lounge Room East", LOUNGE_ROOM_EAST_DESCRIPTION, {}, [], [])
FRONT_VERANDAH_ROOM = Room.Room("Front Verandah", FRONT_VERANDAH_ROOM_DESCRIPTION, {}, [], [])
NAN_ROOM = Room.Room("Side Path", NAN_ROOM_DESCRIPTION, {}, [Items.MOUSE_FIGURINE], [])
STUDY_ROOM = Room.Room("Study", STUDY_ROOM_DESCRIPTION, {}, [], [])

# Create exits.

FRONT_YARD_ROOM.exits = {"w": SIDE_PATH_ROOM, "e": ZOE_CAR_ROOM, "n": FRONT_VERANDAH_ROOM}
SIDE_PATH_ROOM.exits = {"e": FRONT_YARD_ROOM, "n": BACK_GARDEN_ROOM}
ZOE_CAR_ROOM.exits = {"w": FRONT_YARD_ROOM, "n": DRIVEWAY_ROOM}
DRIVEWAY_ROOM.exits = {"s": ZOE_CAR_ROOM, "n": SHED_ROOM, "w": BACK_GARDEN_ROOM}
SHED_ROOM.exits = {"s": DRIVEWAY_ROOM, "n": BACK_GARDEN_ROOM}
BACK_GARDEN_ROOM.exits = {"w": SIDE_PATH_ROOM, "s": BACK_VERANDAH_ROOM, "e": DRIVEWAY_ROOM}
BACK_VERANDAH_ROOM.exits = {"n": BACK_GARDEN_ROOM, "e": LAUNDRY_ROOM}
LAUNDRY_ROOM.exits = {"w": BACK_VERANDAH_ROOM, "e": BATHROOM, "s": GUEST_ROOM}
BATHROOM.exits = {"w": LAUNDRY_ROOM}
KITCHEN.exits = {"w": GUEST_ROOM}
GUEST_ROOM.exits = {"n": LAUNDRY_ROOM, "e": KITCHEN, "s": LOUNGE_ROOM_ENTRY}
MUM_ROOM.exits = {"s": LOUNGE_ROOM_EAST}
LOUNGE_ROOM_ENTRY.exits = {"s": FRONT_VERANDAH_ROOM, "e": LOUNGE_ROOM_EAST, "n": GUEST_ROOM}
LOUNGE_ROOM_EAST.exits = {"n": MUM_ROOM, "s": NAN_ROOM, "e": STUDY_ROOM, "w": LOUNGE_ROOM_ENTRY}
FRONT_VERANDAH_ROOM.exits = {"s": FRONT_YARD_ROOM, "n": LOUNGE_ROOM_ENTRY}
NAN_ROOM.exits = {"n": LOUNGE_ROOM_EAST}
STUDY_ROOM.exits = {"w": LOUNGE_ROOM_EAST}
