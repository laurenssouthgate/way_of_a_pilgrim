class Choice :
    def __init__(self, description, consequnce, condition = lambda p: True):
        self.description = description
        self.consequence = consequnce
        self.condition = condition

    def is_available(self, player) :
        return self.condition(player)
