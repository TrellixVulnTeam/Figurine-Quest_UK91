from game import Room
from game.content import Items
from game.people import Azuri, Gideon, Jay, Molly, Nan, Zoe

# Instantiate rooms first, then create exits. A room must be instantiated to be pointed to as an exit.
FRONT_YARD_ROOM = Room.Room("Front Yard", "Placeholder Front Yard description", {}, [], [])
SIDE_PATH_ROOM = Room.Room("Side Path", "Placeholder Side Path description", {}, [], [])
ZOE_CAR_ROOM = Room.Room("Zoe's Car", "Placeholder Zoe's Car description", {}, [], [])
DRIVEWAY_ROOM = Room.Room("Driveway", "Placeholder driveway description", {}, [], [])
SHED_ROOM = Room.Room("Shed", "Placeholder shed description", {}, [Items.BEAR_FIGURINE], [Molly.Molly])
BACK_GARDEN_ROOM = Room.Room("Back Garden", "Placeholder back garden description", {}, [], [])
BACK_VERANDAH_ROOM = Room.Room("Back Verandah", "Placeholder back verandah description", {}, [], [])
LAUNDRY_ROOM = Room.Room("Laundry Room", "Placeholder laundry room description", {}, [], [])
BATHROOM = Room.Room("Bathroom", "Placeholder bathroom description", {}, [], [])
KITCHEN = Room.Room("Kitchen", "Placeholder kitchen description", {}, [Items.CHOCOLATE], [])
GUEST_ROOM = Room.Room("Guest Room", "Placeholder guest room description", {}, [], [])
MUM_ROOM = Room.Room("Mum's Room", "Placeholder mum's room description", {}, [], [])
LOUNGE_ROOM_ENTRY = Room.Room("Lounge Room Entry", "Placeholder lounge room entry description", {}, [], [])
LOUNGE_ROOM_EAST = Room.Room("Lounge Room East", "Placeholder lounge room east description", {}, [], [])
FRONT_VERANDAH_ROOM = Room.Room("Front Verandah", "Placeholder front verandah description", {}, [], [])
NAN_ROOM = Room.Room("Side Path", "Placeholder Nan's Room description", {}, [Items.MOUSE_FIGURINE], [])
STUDY_ROOM = Room.Room("Study", "Placeholder Study description", {}, [], [])

# Create exits.

FRONT_YARD_ROOM.exits = {"w": SIDE_PATH_ROOM, "e": ZOE_CAR_ROOM, "n": FRONT_VERANDAH_ROOM}
SIDE_PATH_ROOM.exits = {"e": FRONT_YARD_ROOM, "n": BACK_GARDEN_ROOM}
ZOE_CAR_ROOM.exits = {"w": FRONT_YARD_ROOM, "n": DRIVEWAY_ROOM}
DRIVEWAY_ROOM.exits = {"s": ZOE_CAR_ROOM, "n": SHED_ROOM}
SHED_ROOM.exits = {"s": DRIVEWAY_ROOM, "n": BACK_GARDEN_ROOM}
BACK_GARDEN_ROOM.exits = {"w": SIDE_PATH_ROOM, "s": BACK_VERANDAH_ROOM, "e": SHED_ROOM}
BACK_VERANDAH_ROOM.exits = {"n": BACK_GARDEN_ROOM, "e": LAUNDRY_ROOM}
LAUNDRY_ROOM.exits = {"w": BACK_VERANDAH_ROOM, "e": BATHROOM, "s": GUEST_ROOM}
BATHROOM.exits = {"w": LAUNDRY_ROOM}
KITCHEN.exits = {"w": GUEST_ROOM}
GUEST_ROOM.exits = {"n": LAUNDRY_ROOM, "e": KITCHEN, "s": LOUNGE_ROOM_ENTRY}
MUM_ROOM.exits = {"s": LOUNGE_ROOM_EAST}
LOUNGE_ROOM_ENTRY.exits = {"s": FRONT_VERANDAH_ROOM, "e": LOUNGE_ROOM_EAST, "n": GUEST_ROOM}
LOUNGE_ROOM_EAST.exits = {"n": MUM_ROOM, "s": NAN_ROOM, "e": STUDY_ROOM}
FRONT_VERANDAH_ROOM.exits = {"s": FRONT_YARD_ROOM, "n": LOUNGE_ROOM_ENTRY}
NAN_ROOM.exits = {"n": LOUNGE_ROOM_EAST}
STUDY_ROOM.exits = {"w": LOUNGE_ROOM_EAST}
