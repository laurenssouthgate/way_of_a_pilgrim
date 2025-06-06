class Event :
    def __init__(self, name, description) :
        self.name = name
        self.description = description

    def trigger(self, player) -> None :
        raise NotImplementedError("Each event must implement its own trigger method")

