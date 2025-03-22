from art import logo
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """
    Takes a list of cards and returns the total score.
    - If the player has a Blackjack (Ace + 10-value card), return 0.
    - If the score exceeds 21 and the hand contains an Ace (11), convert the Ace to 1.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represents Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # Convert Ace from 11 to 1
        cards.append(1)

    return sum(cards)

# Initialize empty lists to store the player's and computer's cards
user_cards = []
computer_cards = []
is_game_over = False

# Deal two cards to both the player and the computer
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Calculate the initial scores for both players
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

# Display the initial hands and scores
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")  # Hides second card for now

# Check if the game should end immediately (Blackjack or player busts)
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
