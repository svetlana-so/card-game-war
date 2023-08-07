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
        values = list(range(2,15))

        for suit in suits:
            for value in values:
                 card = Card(value, suit)
                 self.cards.append(card)

    def shuffle_cards(self):
         random.shuffle(self.cards)

    def __str__(self):
         return str(self.cards)

def deal_cards(deck):
    half = len(deck.cards)//2
    user_stash = deck.cards[:half]
    computer_stash = deck.cards[half:]
    return user_stash, computer_stash

def draw_card(user_stash, computer_stash):
     players_card = user_stash.pop(0)
     computers_card = computer_stash.pop(0)
     return players_card, computers_card

def main():
     max_iteration = 100
     loop_counter = 0
     deck = Deck()
     greeting()
     user_stash, computer_stash = deal_cards(deck)
     while len(user_stash) > 0 and len(computer_stash) > 0 and loop_counter < max_iteration:
          loop_counter += 1
          players_card, computers_card = draw_card(user_stash, computer_stash)
          print(f"You drew {players_card} and computer drew {computers_card}")
          #press any key to continue
          input('Press enter to continue ')
          compare_cards(players_card,computers_card, user_stash, computer_stash)
          print(f"Your number of cards is: {len(user_stash)}, the computer number of cards is {len(computer_stash)}")
     if loop_counter == max_iteration:
          print("The game has reached the maximum number of iterations. It ends in a draw. ")
     #empthy list = False by defalt
     elif len(user_stash) == 0:
          print("You lost! Computer won the game!")
     elif len(computer_stash) == 0:
          print("Computer lost! You won the game!")
     play_again = input("PLAY AGAIN? (yes/no)")
     if play_again.lower() in ["yes", "y"]:
          main()
     else:
          print("Thank you for playing. BYE!")

def draw_card_while_war(user_stash, computer_stash):
     war_cards =[]
     for x in range(4):
          players_cards = user_stash.pop(0)
          computers_cards = computer_stash.pop(0)
          war_cards.extend([players_cards, computers_cards])
     return war_cards

#compare cards funktion
def compare_cards(players_card,computers_card, user_stash, computer_stash):
     if players_card.value > computers_card.value:
          print("You take the cards!")
          user_stash.extend([players_card, computers_card])

     elif players_card.value < computers_card.value:
          print("Computer take the cards!")
          computer_stash.extend([players_card, computers_card])

     elif players_card.value == computers_card.value:
          print("It is a war! Place three more cards, face-down, on the table and after, flip over a fourth card so that it is face up. ")
          input('Press enter to continue: ')
          if len(user_stash) > 4 and len(computer_stash) > 4:
               war_cards = draw_card_while_war(user_stash, computer_stash)
               u_l_card = war_cards[6]
               c_l_card = war_cards[7]
               print(f"Your fourth card is {u_l_card} and computer's fourth card is {c_l_card}")
               if u_l_card.value > c_l_card.value:
                    user_stash.extend([players_card, computers_card] + war_cards)
                    print("You take the cards!")
               elif u_l_card.value < c_l_card.value:
                    computer_stash.extend([players_card, computers_card] + war_cards)
                    print("Computer take the cards!")
          else:
               if len(user_stash) > len(computer_stash):
                    print("Computer doesn't not enough cards to continue the game. YOU WON!")
                    sys.exit(1)
               elif len(user_stash) < len(computer_stash):
                    print("You don't have enough cards to continue the game. COMPUTER WON!")
                    sys.exit(1)

def typing_text(text, delay=0.03):
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
     typing_text("Press any key to deal the cards and let fate decide your destiny in this epic game of War!")
     input()

if __name__ == "__main__":
    main()