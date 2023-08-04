class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f'{self.value}{self.suit}'  
    
class Deck:
    def __init__(self):
        self.suits = ["heart", "tile", "clover", "spade"] 
        self.values = range(2,16) 
        self.cards = [Card(value, suit) for value in self.values for suit in self.suits]
    def __repr__(self):
        return str(self)
   
               
deck = Deck()
print(deck.cards)