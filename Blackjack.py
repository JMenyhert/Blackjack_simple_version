import random
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
gamer_hand = []
computer_hand = []


def random_card():
    gamer_hand.append(random.choice(cards))


def two_random_card():
    for i in range(2):
        computer_hand.append(random.choice(cards))
        gamer_hand.append(random.choice(cards))


def sum_hand(hand):
    hand_size = 0
    for i in hand:
        hand_size += i
    return hand_size


def blackjack_the_game():

    game_is_on = False

    if input("Do you want to play blackjack? 'y' for yes or 'n' for no. ").lower() == 'y':
        game_is_on = True
    else:
        print("Bye")
        game_is_on = False
    gamer_hand.clear()
    computer_hand.clear()
    two_random_card()

    while game_is_on:
        player_hand_size = sum_hand(gamer_hand)
        computer_hand_size = sum_hand(computer_hand)
        print(f"Your cards: {gamer_hand}, current score:{player_hand_size}")
        print(f"Computer first card: {computer_hand[0]}")
        another_card = input("Do you want another card? 'y' for yes 'n' to pass ").lower()
        if another_card == "y":
            random_card()
            player_hand_size = sum_hand(gamer_hand)
            print(f"Your final hand: {gamer_hand}, your final score is: {player_hand_size}")
            print(f"Computer final hand: {computer_hand}, your final score is: {computer_hand_size}")

        elif another_card == "n":
            print(f"Your final hand: {gamer_hand}, your final score is: {player_hand_size}")
            print(f"Computer final hand: {computer_hand}, your final score is: {computer_hand_size}")

        if player_hand_size > 21:
            print("You went over, you lose.")
        #elif computer_hand_size > player_hand_size and computer_hand_size < 22:
        elif player_hand_size <= computer_hand_size < 22:
            print("Computer win!")
        else:
            print("You win!")

        if input("Do you want to play another game? Type 'y' for restart or 'n' for quit ").lower() == "y":
            blackjack_the_game()
        else:
            print("Thank you for trying the game!")
            game_is_on = False


blackjack_the_game()
