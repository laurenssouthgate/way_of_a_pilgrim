from base_event import Event
from choices import Choice
from utils.choice_utils import present_choices

class ForestStart(Event) :
    def __init__(self) :
        super().__init__(
            name = "Awake in the forest",
            description = "You awake in the forest. Your head is thumping with pain. As you arise from your stupor, you check your knapsack to discover that it is empty. You have been robbed"
        )

        self.choices = [
            Choice("Find the perpetrators and get your things back!", self.revenge),
            Choice("Thank God you are alive", self.pray),
            Choice("Call for help", self.call_for_help),
        ]

    def trigger(self, player) :
        print(self.description)
        print("\nYour inventory is empty")

        player.clear_inventory()
        player.take_damage(15)

        player.show_health()
        player.show_inventory()

        print("\nYou rise to your feet slowly, and gather your senses")

        present_choices(self.choices, player)

    def revenge(self, player) :
        player.decrease_stat("kindness", 10)
        player.increase_stat("wrath", 10)



