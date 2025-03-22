import art
from art import logo
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """
    Takes a list of cards and returns the total score.
    
    - If the player has a Blackjack (Ace + 10-value card), return 0 (indicating an instant win).
    - If an Ace (11) is present and the total score exceeds 21, convert Ace (11) to 1 to prevent busting.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represents Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # Convert Ace from 11 to 1
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    """
    Compares the player's score with the computer's score and determines the winner.
    
    Returns a string message with the game result.
    """
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    """Main function to run a single game of Blackjack."""
    print(logo)  # Print the game logo from `art.py`
    
    # Initialize the player's and computer's hands
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal two initial cards to both player and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Player's Turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show current cards and score
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")  # Only show the first card

        # Check for Blackjack or Bust
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())  # Player takes another card
            else:
                is_game_over = True  # Player stops drawing cards

    # Computer's Turn (only plays if player hasn't busted or won already)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))  # Determine the winner

# Start the game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)  # Clears previous output for better readability
    play_game()
