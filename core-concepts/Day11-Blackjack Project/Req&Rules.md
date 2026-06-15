# 1.Project Goal

    Build a simple Blackjack card game in Python where:
    1. The user plays against the computer.
    2. The computer acts as the dealer.
    3. The goal is to get a score close to 21 without going over.
    4. If a player goes over 21, they lose.
    5. A Blackjack means Ace + 10-value card in the first 2 cards.

# 2. House Rules
    1. The deck is unlimited.
    2. Cards are not removed after drawing.
    3. There are no jokers.
    4. Jack, Queen, and King count as 10.
    5. Ace can count as 11 or 1.
    6. Computer is the dealer.
    7. Computer draws until its score is at least 17.
    8. cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# 3. 10 Quick Summary Points
Blackjack is a card game where the target score is 21.
The user and computer both start with 2 cards.
A card is selected randomly using random.choice().
The card list contains 11 for Ace.
Face cards like Jack, Queen, and King are represented as 10.
A score of 0 is used to represent Blackjack.
If the score is over 21 and the hand has an Ace, Ace changes from 11 to 1.
The user can choose to draw more cards or stop.
The computer keeps drawing cards while its score is less than 17.
The final result is decided using a compare() function.