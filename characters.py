import random


class Character :
    def __init__(self, name, description, events) :
        self.name = name
        self.description = description
        self.events = events

    def interact(self, player):
        if self.events :
            event = random.choice(self.events)
            event.trigger(player)