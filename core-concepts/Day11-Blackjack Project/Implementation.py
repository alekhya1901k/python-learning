# Import the random module
# This module helps generate random values such as random cards
import random


# Define a function to deal a random card
def deal_card():

    # Docstring describing the purpose of this function
    """Returns a random card from the deck"""

    # List representing card values in Blackjack
    # 11 represents Ace
    # 10 appears four times because 10, Jack, Queen, and King are all worth 10 points
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Randomly select one card from the list
    card = random.choice(cards)

    # Return the selected card to the caller
    return card


# Define a function to calculate the score of a hand
def calculate_score(cards):

    # Docstring describing the purpose of this function
    """Take a list of cards and return the score calculated from the cards"""

    # Check if the hand is a Blackjack
    # Blackjack = exactly 21 points with only 2 cards
    if sum(cards) == 21 and len(cards) == 2:

        # Return 0 as a special value representing Blackjack
        return 0

    # Check if the hand contains an Ace (11)
    # and the total score exceeds 21
    if 11 in cards and sum(cards) > 21:

        # Remove one Ace valued at 11
        cards.remove(11)

        # Add the Ace back as value 1
        cards.append(1)

    # Return the total score of the cards
    return sum(cards)


# Define a function to compare user and computer scores
def compare(u_score, c_score):

    # Docstring describing the purpose of this function
    """Compares the user score u_score against the computer score c_score."""

    # If both scores are equal
    if u_score == c_score:
        return "Draw 🙃"

    # If computer has Blackjack
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"

    # If user has Blackjack
    elif u_score == 0:
        return "Win with a Blackjack 😎"

    # If user score exceeds 21
    elif u_score > 21:
        return "You went over. You lose 😭"

    # If computer score exceeds 21
    elif c_score > 21:
        return "Opponent went over. You win 😁"

    # If user score is greater than computer score
    elif u_score > c_score:
        return "You win 😃"

    # Any remaining case means computer wins
    else:
        return "You lose 😤"


# Main function that controls one complete game
def play_game():

    # Create an empty list to store user's cards
    user_cards = []

    # Create an empty list to store computer's cards
    computer_cards = []

    # Initialize computer score
    # -1 is used as a placeholder value
    computer_score = -1

    # Initialize user score
    # -1 is used as a placeholder value
    user_score = -1

    # Variable used to control the game loop
    is_game_over = False

    # Deal two cards each to user and computer
    for _ in range(2):

        # Add a random card to user's hand
        user_cards.append(deal_card())

        # Add a random card to computer's hand
        computer_cards.append(deal_card())

    # Continue playing while game is not over
    while not is_game_over:

        # Calculate user's current score
        user_score = calculate_score(user_cards)

        # Calculate computer's current score
        computer_score = calculate_score(computer_cards)

        # Display user's cards and score
        print(f"Your cards: {user_cards}, current score: {user_score}")

        # Show only computer's first card
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if game should end immediately
        # User Blackjack
        # Computer Blackjack
        # User Bust (>21)
        if user_score == 0 or computer_score == 0 or user_score > 21:

            # End the game loop
            is_game_over = True

        else:

            # Ask the user if they want another card
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            )

            # If user chooses another card
            if user_should_deal == "y":

                # Deal one more card to the user
                user_cards.append(deal_card())

            else:

                # User chooses to stop drawing cards
                is_game_over = True

    # Computer's turn
    # Computer keeps drawing until score reaches at least 17
    while computer_score != 0 and computer_score < 17:

        # Deal another card to computer
        computer_cards.append(deal_card())

        # Recalculate computer score
        computer_score = calculate_score(computer_cards)

    # Display user's final hand and score
    print(f"Your final hand: {user_cards}, final score: {user_score}")

    # Display computer's final hand and score
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}"
    )

    # Compare scores and display result
    print(compare(user_score, computer_score))


# Main game loop
# Allows the player to play multiple rounds
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":

    # Print 20 blank lines
    # Used to simulate clearing the screen
    print("\n" * 20)

    # Start a new Blackjack game
    play_game()