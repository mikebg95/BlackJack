from tkinter import simpledialog
from tkinter import *
from tkinter import messagebox
import time
from gui.gui import Gui

NUM_CARDS = 2


class Round(object):
    def __init__(self, user, dealer, deck, gui):

        print("\n\nNEW ROUND:\n\n")

        ### TO DO: after going past one while loop, it skips it! ###
        # ask player for bet
        bet = simpledialog.askinteger(title="Bet", prompt="How much would you like to bet?")
        while not bet:
            bet = simpledialog.askinteger(title="Bet", prompt="Please insert a bet")
        while bet > user.chips:
            bet = simpledialog.askinteger(title="Bet", prompt="Not enough chips! Try again!")
        while bet < 1:
            bet = simpledialog.askinteger(title="Bet", prompt="Bet must be at least 1!")
        user.chips -= bet
        user.bet = bet

        # show updated player chips info
        gui.chips_label["text"] = "Total chips: " + str(user.chips)
        gui.root.update()

        gui.player_bet["text"] = str(user.bet)
        gui.root.update()

        # deal cards
        for i in range(NUM_CARDS):
            deck.deal_top(user)
            deck.deal_top(dealer)

        # show cards on screen
        gui.player_cards["text"] = user.cards
        gui.dealer_cards["text"] = show_cards(dealer, True)
        gui.root.update()

        first_turn = True  # needed for blackjack check and certain move options
        split = False

        # keep game going with loop
        while True:
            # for hand in user.hands:

            time.sleep(0.5)
            print(f"User points: {user.calculate_score()}")

            # check if user has blackjack
            if first_turn and blackjack(user):
                print("BLACKJACK")
                if not blackjack(dealer):
                    user.chips += 2.5 * user.bet
                    gui.chips_label["text"] = "Total chips: " + str(user.chips)
                    break
                else:
                    print("BOTH BLACKJACK")
                    user.chips += user.bet
                    gui.chips_label["text"] = "Total chips: " + str(user.chips)
                    break

            # check if score higher than 21
            if user.calculate_score() > 21:
                print("MORE THAN 21! YOU LOSE")
                break

            # players move
            move = StringVar()

            def option_chosen(m):
                global move_picked
                move_picked = m

            # show move options
            options = ["hit", "stand", "double", "split"]
            if user.cards[0].score != user.cards[1].score:
                options.remove("split")
            if user.chips < user.bet or not first_turn:
                options.remove("double")

            # present move options to player
            for option in options:
                Radiobutton(gui.player_options_frame, text=option, variable=move, value=option, indicator=0,
                            command=lambda: option_chosen(move.get())).pack()

            print("Waiting for move...")

            # wait until option is chosen before continuing loop
            gui.root.wait_variable(move)

            if move_picked == "stand":
                gui.dealer_cards["text"] = dealer.cards
                gui.root.update()
                print("Player chose STAND")
                time.sleep(0.5)

                dealer_turn(dealer, gui, deck)
                check_winner(user, dealer, gui)
                break

            if move_picked == "double":
                user.chips -= bet
                gui.chips_label["text"] = "Total chips: " + str(user.chips)
                bet *= 2
                user.bet = bet
                gui.player_bet["text"] = str(user.bet)

                deck.deal_top(user)
                gui.player_cards["text"] = user.cards
                gui.root.update()

                if user.calculate_score > 21:
                    print("PLAYER > 21! YOU LOSE!")
                    break

                dealer_turn(dealer, gui, deck)
                check_winner(user, dealer, gui)
                break

            # hit
            deck.deal_top(user)
            gui.player_cards["text"] = user.cards
            gui.root.update()

            first_turn = False

            # empty options
            for widget in gui.player_options_frame.winfo_children():
                widget.destroy()


def show_cards(player, dealer=False):
    cards = []
    if len(player.cards) != 0:
        if dealer:
            cards = player.show_cards(True)
        else:
            cards = player.show_cards(False)
    return cards


def blackjack(player):
    total = 0
    for card in player.cards:
        total += card.score
    if total == 21:
        return True
    else:
        return False


def dealer_turn(dealer, gui, deck):
    # dealers turn
    print("Dealers turn:")
    print(f"Dealer has {dealer.calculate_score()}")
    time.sleep(1)

    while True:
        if dealer.calculate_score() > 21:
            print("DEALER > 21")
            time.sleep(0.5)
            break
        if dealer.calculate_score() < 17:
            print("Dealer takes another card")
            deck.deal_top(dealer)
            gui.dealer_cards["text"] = dealer.cards
            gui.root.update()
            time.sleep(0.5)
        if dealer.calculate_score() >= 17:
            print(f"Dealer no more cards. Dealer score: {dealer.calculate_score()}")
            time.sleep(0.5)
            break

    gui.dealer_cards["text"] = dealer.cards
    gui.root.update()
    return


def check_winner(user, dealer, gui):
    user_score = user.calculate_score()
    dealer_score = dealer.calculate_score()
    print(f"\nUSER: {user_score}")
    print(f"\nDEALER: {dealer_score}")
    if dealer_score > 21:
        print("DEALER > 21! YOU WIN")
        user.chips += 2 * user.bet
        gui.chips_label["text"] = "Total chips: " + str(user.chips)
    elif user_score > dealer_score:
        print("YOU WIN")
        user.chips += 2 * user.bet
        gui.chips_label["text"] = "Total chips: " + str(user.chips)
    elif user_score < dealer_score:
        print("YOU LOSE")
    else:
        print("TIE")
        user.chips += user.bet
        gui.chips_label["text"] = "Total chips: " + str(user.chips)
