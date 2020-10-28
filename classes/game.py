from classes.deck import Deck
from tkinter import simpledialog
from classes.player import Player
from tkinter import *
from classes.round import Round
from tkinter import messagebox
import time

class Game(object):
    def __init__(self, gui):

        self.rounds = []

        # create deck
        deck = Deck()

        # popup window to ask for name, create player objects
        name = simpledialog.askstring(title="Name", prompt="What's your name?")
        while not name:
            name = simpledialog.askstring(title="Name", prompt="Please insert a name")
        players = []
        user = Player(name)
        dealer = Player("Dealer")
        players.append(user)
        players.append(dealer)

        # show player info
        gui.name_label["text"] = "Name: " + user.name
        gui.chips_label["text"] = "Total chips: " + str(user.chips)

        # start new round as long as user has enough chips
        while user.chips >= 1:
            user.cards.clear()
            dealer.cards.clear()

            current_round = Round(user, dealer, deck, gui)

            self.rounds.append(current_round)

            new_round = messagebox.askquestion("New game?")
            if new_round == "no":
                gui.root.destroy()

            # empty options
            for widget in gui.player_options_frame.winfo_children():
                widget.destroy()

            # empty user cards
            user.cards.clear()
            dealer.cards.clear()
        messagebox.showinfo("GAME OVER", "OUT OF CHIPS!")
