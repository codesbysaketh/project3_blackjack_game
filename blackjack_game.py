import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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

def gameplay_choice():
    global game, service
    player.clear()
    dealer.clear()
    play_choice = input("Type y to play again or n to quit : ")
    if play_choice == "y":
        game = False
        service = True
    else:
        game = False
        service = False

def show():
    print(f"Player cards {player}")
    print(f"Dealer cards {dealer}")

print(logo)
print("Welcome to blackjack game!!")


player = []
player_sum = 0
dealer = []
dealer_sum = 0

service = True
game = True

while service:

    game = True
    for _ in range(2):
        player.append(random.choice(cards))
        dealer.append(random.choice(cards))
    
    player_sum = sum(player)    
    dealer_sum = sum(dealer)
    
    print(f"Your cards are {player}")
    print(f"Dealers card is {dealer[0]}")

    if player_sum == 21:
        print("You win!!!!")
        game = False
    elif player_sum > 21:
        print("You cards exceed 21, You lose")
        game = False

    while game:
        choice = input("Type hit to get a new card and stand to play with existing ones : ").lower()
        if choice == "hit":
            player.append(random.choice(cards))
            print(f"Your new cards are {player}")
            dealer.append(random.choice(cards))

            player_sum = sum(player)
            dealer_sum = sum(dealer)

            if player_sum == 21:
                show()
                print("You win!!!!")
                gameplay_choice()
            elif player_sum > 21:
                show()
                print("You cards exceed 21, You lose")
                gameplay_choice()

        elif choice == "stand":
            if dealer_sum <= 16:
                dealer.append(random.choice(cards))
                dealer_sum = sum(dealer)
            if (21 - player_sum) < (21 - dealer_sum):
                show()
                print("You win!!!")
                gameplay_choice()
            elif (21 - player_sum) == (21 - dealer_sum):
                show()
                print("Draw.")
                gameplay_choice()
            else:
                show()
                print("You lose.")
                gameplay_choice()






