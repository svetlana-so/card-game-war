import random
import time
import sys

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

def main():
     deck = Deck()
     greeting()
     user_cards, computer_cards = deal_cards(deck)

     

def deal_cards(deck):
    half = len(deck.cards)//2
    return [str(card) for card in deck.cards][:half], [str(card) for card in deck.cards][half:]


def typing_text(text, delay=0.07):
     for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
     print()

def greeting():
     typing_text("Welcome to the card game War!")
     typing_text("Today, you are in for an exciting challenge as you face off against the computer.")
     typing_text("Get ready for a thrilling battle of cards as you try to conquer and triumph over your digital opponent.")
     typing_text("Without further ado, let the battle commence!")
     typing_text("Press any key to deal the cards and let fate decide your destiny in this epic game of War! May the best player prevail!")
     input()



if __name__ == "__main__":
    main()