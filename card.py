# Name:Cristian Leon

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"Card(value={self.value},suit={self.suit})"

    def __str__(self):
        return f"{self.value} of {self.suit}"
    
    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False
    
    
