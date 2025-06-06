import random

class Location :
    def __init__(self, name, description, intro, events = None, characters = None):
        self.name = name
        self.description = description
        self.intro = intro
        self.events = events or []
        self.characters = characters or []

    def visit(self, player) :
        print(f"You have arrived at {self.name}")

        if self.events and random.random() < 0.5 :
            random.choice(self.events).trigger(player)

        if self.characters and random.random() < 0.5 :
            character = random.choice(self.characters)

locations = {
    "Forest" : Location(
        name = "Forest",
        description = "",
        intro = "You are walking along a dusty track in the middle of a forest. The tall pine trees stand on either side. You can hear the birds singing as the sun begins to climb above the tree tops."
    ) 
}