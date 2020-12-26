from game import Item

# Quest items
DOG_FIGURINE = Item.Item("dog figurine", ["dog", "figurine", "figure"], "This is a dog figurine.",
                         "This is a small garden ornament in the shape of a dog. Nan's probably "
                         "looking for this.", False, False) # Gideon has this.
PIG_FIGURINE = Item.Item("pig figurine", ["pig", "figurine", "figure"], "This is a pig figurine.",
                         "This is a small garden ornament in the shape of a pig. Nan's probably "
                         "looking for this.", False, False) # Azuri has this.
CAT_FIGURINE = Item.Item("cat figurine", ["cat", "figurine", "figure"], "This is a cat figurine.",
                         "This is a small garden ornament in the shape of a cat. Nan's probably "
                         "looking for this.", True, True) #  TODO: Find place for this.
MOUSE_FIGURINE = Item.Item("mouse figurine", ["mouse", "figurine", "figure"], "This is a mouse figurine.",
                           "This is a small garden ornament in the shape of a mouse. Nan's probably "
                           "looking for this.", True, True) # TODO: Find place for this.
BEAR_FIGURINE = Item.Item("bear figurine", ["bear", "figurine", "figure"], "This is a bear figurine.",
                          "This is a small garden ornament in the shape of a bear. Nan's probably "
                          "looking for this.", True, True) # Molly has this in the shed.

# Quest-associated items
CAT_TOY = Item.Item("cat toy", ["cat", "toy"], "This is a cat toy.",
                    "This is a toy that Azuri loves. Maybe you could give it to her to make her come out of hiding?",
                    True, True)
CHOCOLATE = Item.Item("chocolate", ["choc", "lokalet"], "This is a piece of chocolate.",
                      "This is a piece of chocolate. Maybe a certain small person would like you to give it to them?",
                      True, True)

# Flavor items
