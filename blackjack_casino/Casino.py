
import random
def blackjack():

    NUM_DECKS = 6

    num_games = 1
    players_win = 0
    dealers_win = 0
    num_ties = 0

    shoe = []

    def reset_shoe():
        shoe.clear()
        # 6 decks, 4 suits, ranks 1..13
        for _ in range(NUM_DECKS * 4):
            shoe.extend(range(1, 14))
        random.shuffle(shoe)

    def draw_card():
        if len(shoe) < 15:
            reset_shoe()
        return shoe.pop()

    def card_name(val):
        return {1: "ACE", 11: "JACK", 12: "QUEEN", 13: "KING"}.get(val, str(val))

    def hand_value(cards):
        total = 0
        aces = 0
        for r in cards:
            if r == 1:
                total += 11
                aces += 1
            elif r in (11, 12, 13):
                total += 10
            else:
                total += r
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def show_draw(prefix, card, hand_total):
        print(f"{prefix} {card_name(card)}!")
        print(f"Your hand is: {hand_total}\n")

    def menu():
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit\n")

    def print_stats():
        games_played = num_games - 1
        pct = (players_win / games_played) * 100 if games_played > 0 else 0.0
        print(f"Number of Player wins: {players_win}")
        print(f"Number of Dealer wins: {dealers_win}")
        print(f"Number of tie games: {num_ties}")
        print(f"Total # of games played is: {games_played}")
        print(f"Percentage of Player wins: {pct:.1f}%\n")

    reset_shoe()
    running = True

    while running:
        print(f"START GAME #{num_games}\n")

        player = [draw_card(), draw_card()]
        dealer = [draw_card(), draw_card()]

        # show player's initial two draws like a real game
        show_draw("Your card is a", player[0], hand_value([player[0]]))
        show_draw("Your card is a", player[1], hand_value(player))

        p_total = hand_value(player)
        d_total = hand_value(dealer)

        # check natural blackjack
        if p_total == 21 or d_total == 21:
            print(f"Dealer shows: {card_name(dealer[0])} and a hidden card")
            print(f"Dealer's hand: {d_total}")
            print(f"Your hand is: {p_total}\n")
            if p_total == 21 and d_total == 21:
                print("It's a tie! No one wins!\n")
                num_ties += 1
            elif p_total == 21:
                print("BLACKJACK! You win!\n")
                players_win += 1
            else:
                print("Dealer wins!\n")
                dealers_win += 1
            num_games += 1
            continue

        # in-hand menu
        while True:
            menu()
            sel = input("Choose an option: ")
            if not sel.isdigit() or not (1 <= int(sel) <= 4):
                print("\nInvalid input!\nPlease enter an integer value between 1 and 4.\n")
                continue
            sel = int(sel)

            if sel == 1:
                c = draw_card()
                player.append(c)
                p_total = hand_value(player)
                show_draw("Your card is a", c, p_total)
                if p_total > 21:
                    print("You exceeded 21! You lose.\n")
                    dealers_win += 1
                    num_games += 1
                    break
                if p_total == 21:
                    print("BLACKJACK! You win!\n")
                    players_win += 1
                    num_games += 1
                    break

            elif sel == 2:
                # dealer plays: stand on soft 17
                print(f"\nDealer shows: {card_name(dealer[0])} and a hidden card")
                while hand_value(dealer) < 17:
                    dealer.append(draw_card())
                d_total = hand_value(dealer)
                print(f"Dealer's hand: {d_total}")
                print(f"Your hand is: {p_total}\n")

                if d_total > 21:
                    print("You win!\n")
                    players_win += 1
                elif p_total > d_total:
                    print("You win!\n")
                    players_win += 1
                elif d_total > p_total:
                    print("Dealer wins!\n")
                    dealers_win += 1
                else:
                    print("It's a tie! No one wins!\n")
                    num_ties += 1

                num_games += 1
                break

            elif sel == 3:
                print_stats()

            elif sel == 4:
                running = False
                break
blackjack()