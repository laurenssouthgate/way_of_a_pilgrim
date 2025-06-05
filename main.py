from player import Player

def create_player() :
    print("Welcome, pilgrim.")
    name = input("Please enter your name: ")
    player = Player(name)
    print("Your spiritual journey begins...")