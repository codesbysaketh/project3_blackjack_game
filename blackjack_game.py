import random
import os

logo = """
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
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ This function calculates the sum of cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_score, dealer_score):
    if player_score ==  dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lose dealer has blackjack :("
    elif player_score == 0:
        return "You win!!! with a blackjack :))"
    elif player_score > 21:
        return "You went over 21, you lose"
    elif dealer_score > 21:
        return "Dealer went over 21, You win!!"
    elif player_score > dealer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    is_game_over = False
    player = []
    dealer = []

    for _ in range(2):
        player.append(deal_card())
        dealer.append(deal_card())

    while not is_game_over:
        player_sum = calculate_score(player)
        dealer_sum = calculate_score(dealer)

        print(f"Player cards are {player} and sum is {player_sum}")
        print(f"Dealers faceup card is {dealer[0]}")

        if player_sum == 0 or dealer_sum == 0 or player_sum > 21:
            is_game_over = True
        else:
            user_deal_choice = input("Type hit to add another card or stand to play with existing cards : ")
            if user_deal_choice == "hit":
                player.append(deal_card())
            else:
                is_game_over = True

    while dealer_sum != 0 and dealer_sum < 17:
        dealer.append(deal_card())
        dealer_sum = calculate_score(dealer)

    print(f"Your final hand is {player} and score {player_sum}")
    print(f"Dealer's final hand is {dealer} and his score is {dealer_sum}")

    print(compare(player_sum, dealer_sum))

while input("Do you want to play again type y or n : ") == "y":
    os.system('cls')
    play_game()
