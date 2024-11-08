import random

# ASCII logo for the Blackjack game
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    """Returns a randomly selected card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates and returns the score for the provided hand of cards.
    Aces (11) are adjusted to 1 if the score exceeds 21."""
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0  # 0 represents a Blackjack
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the user and computer scores and returns the result message."""
    if user_score == computer_score:
        return "It's a Draw."
    elif computer_score == 0:
        return "Computer has Blackjack! You lose."
    elif user_score == 0:
        return "You have Blackjack! You win!"
    elif user_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    """Plays a single game of Blackjack."""
    print(logo)

    # Initial deal: two cards each for user and computer
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    
    game_over = False

    # User turn
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for end-of-game conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Game loop for replaying
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 3)  # Clears console for readability
    play_game()
