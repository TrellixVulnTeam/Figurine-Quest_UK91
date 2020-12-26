from game import Constants


class Player:

    # Location: Room object the player is currently in.
    # Inventory: List of Item objects the player currently holds.
    def __init__(self, location, inventory):
        self.location = location
        self.inventory = inventory

    # Prints a list of all items in the player's inventory.
    def get_inventory(self):
        description = Constants.INVENTORY_START_STRING + "\n"
        if len(self.inventory) == 0:
            description += Constants.EMPTY_INVENTORY_STRING
            return description
        for item in self.inventory:
            description += item.name
            if item != self.inventory[-1]:  # Add a new line unless it is the last item.
                description += "\n"
        return description

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    # Move to another room. Uses the room's code. Here for potential added features and readability.
    def move_room(self, direction):
        current_room = self.location
        if direction in current_room.exits:
            self.location = current_room.exits[direction]
            return current_room.exits[direction].enter_room()
        else:
            return Constants.EXIT_NOT_FOUND_STRING
