import random
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f"{self.value}{self.figure()}"

    def figure(self):
        suit_lower = self.suit.lower()
        if suit_lower == "heart":
                return "♥️"
        elif suit_lower == "tile":
                return "♦️"
        elif suit_lower == "clover":
                return "♣️"
        elif suit_lower == "spade":
                return "♠️"
        else:
             return ""

class Deck():
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle_cards()

    def create_deck(self):
        suits = ["heart", "clover", "spade", "tile"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for value in values:
                 card = Card(value, suit)
                 self.cards.append(card)

    def shuffle_cards(self):
         random.shuffle(self.cards)

    def __str__(self):
         return str([str(card) for card in self.cards])


deck = Deck()
print(deck)