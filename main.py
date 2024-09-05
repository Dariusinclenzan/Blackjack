import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Do you wanna play a game of blackjack? Y/N: ").lower()
user_cards = []
computer_cards = []
total_user = 0
total_computer = 0

if start == "y":
    for card in range(2):
        user_draw = random.choice(cards)
        computer_draw = random.choice(cards)
        user_cards.append(user_draw)
        computer_cards.append(computer_draw)
        total_user += user_draw
        total_computer += computer_draw
    print(f"Your cards are {user_cards}")
    print(f"Computer cards are {computer_cards}")
    another_hand = True
    while another_hand:

        if total_user < 21 and total_computer < 21:
            another_go = input("Would you like to draw another hand? Y/N: ").lower()
            if another_go == "y":
                for card in range(1):
                    user_draw = random.choice(cards)
                    computer_draw = random.choice(cards)
                    user_cards.append(user_draw)
                    computer_cards.append(computer_draw)
                    total_user += user_draw
                    total_computer += computer_draw
                print(f"Your cards are {user_cards}")
                print(f"Computer cards are {computer_cards}")
            elif another_go == "n":
                print(f"Your total is {total_user}")
                print(f"Computer total is {total_computer}")
                another_hand = False
                if total_user > total_computer:
                    print("You won")
                elif total_user == total_computer:
                    print("Draw")
                else:
                    print("Computer won")

        else:
            if total_user > 21:
                print("You went over 21, computer won")
                another_hand = False
            elif total_computer > 21:
                print("Computer went over 21, you won")
                another_hand = False






