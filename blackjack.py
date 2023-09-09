import random
from replit import clear
from art import logo
import sys

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_status = True

while game_status == True:
    
    user_cards = []
    computer_cards = []

    def deal_card(random_cards):
        random_card = random.choice(cards)
        return random_card

    def calculate_score(cards):
        for i in cards:
            if i == 11 and sum(cards) > 21:
                cards.remove(11)
                cards.append(1)
        cards_sum = sum(cards)
        if cards_sum == 21:
            return 0
        else:
            return cards_sum

    game_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if game_play == "y":
        print(logo)
        user_cards.append(deal_card(user_cards))
        user_cards.append(deal_card(user_cards))
        computer_cards.append(deal_card(computer_cards))
        computer_cards.append(deal_card(computer_cards))

        user_sum = calculate_score(user_cards)
        computer_sum = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"Computer's first card: {computer_cards[0]}")
    else:
        sys.exit()

    draw_again = ""

    if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0 or calculate_score(user_cards) > 21:
        game_status = False

    while calculate_score(user_cards) < 21 and game_status == True and calculate_score(user_cards) != 0:
        draw_again = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
        if draw_again == "y":
            user_cards.append(deal_card(user_cards))
            user_sum = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_sum}")
            print(f"Computer's first card: {computer_cards[0]}")
        else:
            game_status = False

    while computer_sum < 17 and user_sum != 21 and user_sum < 21:
        computer_cards.append(deal_card(computer_cards))
        computer_sum = calculate_score(computer_cards)
        
    def compare(user_sum, computer_sum):
        if user_sum == 0:
            print(f"Your final hand: {user_cards}, final score: {user_sum}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
            print("Blackjack! Nice hand cowboy, you win!")
            game_status = False
        elif computer_sum == 0:
            print(f"Your final hand: {user_cards}, final score: {user_sum}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
            print("Ouch, bad luck outlaw. Dealer hit a blackjack. You lose.")
            game_status = False
        elif user_sum > 21:
            print(f"Your final hand: {user_cards}, final score: {user_sum}")
            print("Man.. You went over. You lose.")
            game_status = False
        elif user_sum == computer_sum:
            print(f"Your final hand: {user_cards}, final score: {user_sum}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
            print("You tied with the house. It's a draw!")
            game_status = False
        elif computer_sum > 21:
            print(f"Your final hand: {user_cards}, final score: {user_sum}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
            print("Dealer went bust! You win!")
            game_status = False
        elif user_sum > computer_sum:
            print(f"Your final hand: {user_cards}, final score: {user_sum}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
            print("Well, looks like the dealer's done drawing cards. You win!")
            game_status = False
        else:
            print(f"Your final hand: {user_cards}, final score: {user_sum}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")
            print("You lose.")
            game_status = False

    compare(user_sum, computer_sum)

    restart_game = input("Do you want to restart and play again? Type 'y' or 'n': ").lower()
    if restart_game == "y":
        clear()
        print(logo)
        game_status = True
    else:
        sys.exit()
