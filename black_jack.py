import random

def draw_card(hand, deck):
    hand.append(deck.pop())  

def calculate_score(hand):
    total = 0
    aces = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            aces += 1
        else:
            total += int(card)

    #ACES
    for _ in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1

    return total

def main():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    player_hand = []
    dealer_hand = []

    random.shuffle(deck)


    draw_card(dealer_hand, deck)      
    draw_card(player_hand, deck)      
    draw_card(player_hand, deck)

    print("Dealer shows:", dealer_hand[0])
    print("Your hand:", player_hand, "score =", calculate_score(player_hand))

    #PLAYER CHOICE
    while True:
        choice = input("Hit or stay? (h/s): ").lower()

        if choice == "h":
            draw_card(player_hand, deck)
            score = calculate_score(player_hand)
            print("Your hand:", player_hand, "score =", score)

            if score > 21:
                print("You bust! Dealer wins.")
                return

        elif choice == "s":
            break
        else:
            print("Invalid choice.")

    #DEALER CHOICE
    print("\nDealer's turn...")
    print("Dealer hand:", dealer_hand, "score =", calculate_score(dealer_hand))

    while calculate_score(dealer_hand) < 17:
        draw_card(dealer_hand, deck)
        print("Dealer draws:", dealer_hand, "score =", calculate_score(dealer_hand))

        if calculate_score(dealer_hand) > 21:
            print("Dealer busts! You win.")
            return

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\nFinal hands:")
    print("Your hand:", player_hand, "score =", player_score)
    print("Dealer hand:", dealer_hand, "score =", dealer_score)

    if player_score > dealer_score:
        print("You win!")
    elif dealer_score > player_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
