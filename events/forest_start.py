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
        player.decrease_stat("kindness", 7)
        player.decrease_stat("temperance", 5)
        player.decrease_stat("humility", 7)
        player.increase_stat("wrath", 10)
        player.increase_stat("pride", 7)

        print("\nYou give in to the sense of anger at the situation, and begin in earnest to search the surroundings for any sign that might lead to you the perpetrators")
        print("\nYou notice two sets of footprints going off along the path")

        choices = [
            Choice("Follow the footprints and see where they lead", follow(player)),
            Choice("Give it up and commit yourself to God", give_up(player))
        ]

        present_choices(choices, player)

        def follow(player) :
            pass

        def give_up(player) :
            pass 
    
    def pray(self, player) :
        player.increase_stat("dilligence", 3)
        player.increase_stat("humility", 5)
        player.decrease_stat("pride", 5)

        print("\nYou make the sign of the cross and bow your head. 'God forgive them, and forgive me a sinner' you say. You make your way back to the path.")

        choices = [
            Choice("Go right", go_right(player)),
            Choice("Go left", go_left(player))
        ]

        present_choices(choices, player)

        def go_right(player) :
            pass

        def go_left(player) :
            pass

    def call_for_help(self, player) :
        pass



