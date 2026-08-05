import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    score = sum(card_list)

    # Blackjack: 21 with exactly 2 cards
    if score == 21 and len(card_list) == 2:
        return 0

    # Change Ace from 11 to 1 if score is over 21
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)

    return score


def compare(user_score, computer_score):

    if user_score == computer_score:
        return "It's a Draw!"

    elif computer_score == 0:
        return "You lose! Computer has a Blackjack."

    elif user_score == 0:
        return "You win with a Blackjack!"

    elif user_score > 21:
        return "You went over 21. You lose!"

    elif computer_score > 21:
        return "Computer went over 21. You win!"

    elif user_score > computer_score:
        return "You win!"

    else:
        return "You lose!"


def play_game():

    user_cards = []
    computer_cards = []
    game_over = False

    # Give 2 cards each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}")
        print(f"Your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End game if someone has Blackjack or user goes over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            choice = input(
                "Type 'y' to get another card, 'n' to pass: "
            )

            if choice == "y":
                user_cards.append(deal_card())

            else:
                game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final result
    print("\n============= Final Result =============")
    print(f"Your cards: {user_cards}")
    print(f"Your final score: {user_score}")

    print(f"\nComputer cards: {computer_cards}")
    print(f"Computer final score: {computer_score}")

    print(compare(user_score, computer_score))


# Play again loop
while True:

    play_game()

    again = input( "\nDo you want to play again? Type 'y' or 'n': " )

    if again == "n":
        print("Thanks for playing!")
        break
