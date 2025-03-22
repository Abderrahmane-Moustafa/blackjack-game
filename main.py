from art import logo
import random
#choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")




def deal_card():
    """Return a random card from the dictionary"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

"""Define 2 var for the user card and the computer card"""
user_cards = []
computer_cards = []

"""Add 2 random cards to the user and the comouter"""
for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(new_card)

print(user_cards, computer_cards)



