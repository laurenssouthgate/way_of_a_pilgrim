from choices import Choice
from player import Player

def present_choices(player: Player, choices: list[Choice]) :
    available_choices = [choice for choice in choices if choice.is_available(player)]

    if not available_choices :
        print("There is nothing you can do here.")
        return
    
    for i, choice in enumerate(available_choices, 1) :
        print(f"{i}. {choice.description}")

    while True :
        try:
            selection = int(input("\nWhat do you want to do?: (Enter number)"))
            if 1 <= selection <= len(available_choices):
                available_choices[selection - 1].consequence(player)
                break
        except ValueError:
            pass
        print("Invalid input. Please enter a valid number.")