class Player :
    def __init__(self, name):
        self.name = name

        self.obedience = 50
        self.watchfulness = 50
        self.prayerFocus = 50
        self.humility = 50

        self.pride = 0
        self.anger = 0
        self.delusion = 0
        self.greed = 0

        self.inventory = ["psalter", "prayer rope"]
        self.journal = []


