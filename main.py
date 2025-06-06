from player import Player
import random

def create_player() :
    print("Welcome, pilgrim.")
    name = input("Please enter your name: ")
    
    while True :
        player = Player(name)
        print("Here are your initial stats:")
        player.show_stats()

        choice = input("Would you like to keep these stats? (y/n)").strip().lower()
        if choice in ['yes', 'y'] :
            print("Your spiritual journey begins...")
            return player
        elif choice in ['no', 'n'] :
            print("Re-rolling your stats...")
        else :
            print("Invalid input")

def set_starting_location() :
    return None

def main() :
    player = create_player()

if __name__ == "__main__":
    main()