import random

class Player :
    def __init__(self, name):
        self.name = name

        self.chastity = random.randint(40, 60)
        self.temperance = random.randint(40, 60)
        self.charity = random.randint(40, 60)
        self.diligence = random.randint(40, 60)
        self.patience = random.randint(40, 60)
        self.kindness = random.randint(40, 60)
        self.humility = random.randint(40, 60)

        self.lust = random.randint(0, 20)
        self.gluttony = random.randint(0, 20)
        self.greed = random.randint(0, 20)
        self.sloth = random.randint(0, 20)
        self.wrath = random.randint(0, 20)
        self.envy = random.randint(0, 20)
        self.pride = random.randint(0, 20)

        self.health = 100
        self.inventory = ["Psalter", "Prayer rope"]
        self.journal = []

    def show_stats(self) :
        print(f"Pilgrim {self.name}'s spiritual state:")
        print("Virtues:")
        print(f"Chastity: {self.chastity}")
        print(f"Temperance: {self.temperance}")
        print(f"Charity: {self.charity}")
        print(f"Diligence: {self.diligence}")
        print(f"Patience: {self.patience}")
        print(f"Kindness: {self.kindness}")
        print(f"Humility: {self.humility}")
        print("Vices:")
        print(f"Lust: {self.lust}")
        print(f"Gluttony: {self.gluttony}")
        print(f"Greed: {self.greed}")
        print(f"Sloth: {self.sloth}")
        print(f"Wrath: {self.wrath}")
        print(f"Envy: {self.envy}")
        print(f"Pride: {self.pride}")

    def show_health(self) :
        print(f"Your health is at: {self.health}")

    def show_inventory(self) :
        if not self.inventory :
            print("You have nothing in your inventory")
        else :
            for item in self.inventory :
                print(item)

    def take_damage(self, amount) :
        self.health = max(self.health - amount, 0)

    def increase_stat(self, stat, amount) :
        if hasattr(self, stat) :
            current = getattr(self, stat)
            new_val = max(0, min(100, current + amount))
            setattr(self, new_val)
        else :
            print(f"Error stat: {stat} doesn't exist")

    def decrease_stat(self, stat, amount) :
        if hasattr(self, stat) :
            current = getattr(self, stat)
            new_val = max(0, min(100, current - amount))
            setattr(self, new_val)
        else :
            print(f"Error stat: {stat} doesn't exist")

    def clear_inventory(self) :
        self.inventory = []
        

