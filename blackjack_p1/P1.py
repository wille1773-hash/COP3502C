import p1_random as p1

rng = p1.P1Random()
num_games = 1
players_win = 0
dealers_win = 0
num_ties = 0

def start():
    print(f"START GAME #{num_games}")

def card_name(val):
    if val == 1:
        return "ACE"
    elif val == 11:
        return "JACK"
    elif val == 12:
        return "QUEEN"
    elif val == 13:
        return "KING"
    else:
        return str(val)

def card_value(val):
    if val == 1:
        return 1
    elif val in (11, 12, 13):
        return 10
    else:
        return val

def your_cardhand(card_value, hand_value):
    print(f"\nYour card is a {card_name(card_value)}!")
    print(f"Your hand is: {hand_value}\n")

def menu():
    print('''1. Get another card
2. Hold hand
3. Print statistics
4. Exit
    ''')

def print_stats():
    games_played = num_games - 1
    if games_played > 0:
        pct = (players_win / games_played) * 100  
    else:
        pct = 0.0
    print(f"\nNumber of Player wins: {players_win}")
    print(f"Number of Dealer wins: {dealers_win}")
    print(f"Number of tie games: {num_ties}")
    print(f"Total # of games played is: {games_played}")
    print(f"Percentage of Player wins: {pct:.1f}%\n")

running = True

while running:
    players_hand = 0
    start()
    players_card = rng.next_int(13) + 1
    players_hand += card_value(players_card)
    your_cardhand(players_card, players_hand)

    while True:
        menu()
        menu_selection = int(input(f"Choose an option: "))
        if menu_selection < 1 or menu_selection > 4:
            print("Invalid input!")
            print()
            print("Please enter an integer value between 1 and 4.")
            continue
        if menu_selection == 1:
            players_card = rng.next_int(13) + 1
            players_hand += card_value(players_card)
            your_cardhand(players_card, players_hand)
            if players_hand > 21:
                print("You exceeded 21! You lose.\n")
                dealers_win += 1
                num_games += 1
                break
            elif players_hand == 21:
                print("BLACKJACK! You win!\n")
                players_win += 1
                num_games += 1
                break
        elif menu_selection == 2:
            dealers_hand = rng.next_int(11) + 16
            print(f"\nDealer's hand: {dealers_hand}")
            print(f"Your hand is: {players_hand}\n")
            if dealers_hand > 21:
                print("You win!\n")
                num_games +=1
                players_win += 1
            elif players_hand > dealers_hand:
                print("You win!\n")
                players_win += 1
                num_games += 1
            elif dealers_hand > players_hand:
                print("Dealer wins!\n")
                dealers_win += 1
                num_games += 1
            else:
                print("It's a tie! No one wins!\n")
                num_ties +=1
                num_games +=1
            break
        elif menu_selection == 3:
            print_stats()
        elif menu_selection == 4:
            running = False
            break
    
    