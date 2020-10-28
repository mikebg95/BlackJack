from tkinter import *

BG_COLOR = "#4a941c"
HIGHLIGHT_FRAME = {
    'highlightthickness' : 1,
    'highlightcolor' : '#FFFFFF',
    'highlightbackground' : '#FFFFFF'
}


class Gui(object):
    def __init__(self):

        self.root = Tk()
        self.root.title("BlackJack")
        self.root.geometry("720x720")
        self.root.iconbitmap("../icon/blackjack.ico")
        self.root.configure(bg=BG_COLOR)

        self.player_frame = LabelFrame(self.root, bg=BG_COLOR, **HIGHLIGHT_FRAME, width=720, height=300)
        self.player_frame.pack(side=BOTTOM, padx=10, pady=10)
        self.player_frame.pack_propagate(0) # make sure frame stays same size

        self.player_options_frame = LabelFrame(self.player_frame, bg=BG_COLOR, **HIGHLIGHT_FRAME, width=200, height=200)
        self.player_options_frame.pack(side=LEFT, padx=10, pady=10)

        self.player_info_frame = LabelFrame(self.player_frame, bg=BG_COLOR, **HIGHLIGHT_FRAME, width=200, height=200)
        self.player_info_frame.pack(side=RIGHT, padx=10, pady=10)

        self.player_cards_frame = LabelFrame(self.player_frame, bg=BG_COLOR, **HIGHLIGHT_FRAME, width=100, height=100)
        self.player_cards_frame.pack(side=TOP, padx=10, pady=10)

        self.player_entry_frame = LabelFrame(self.player_frame, bg=BG_COLOR, **HIGHLIGHT_FRAME, width=200, height=100)
        self.player_entry_frame.pack(side=BOTTOM, padx=10, pady=10)

        self.dealer_frame = LabelFrame(self.root, bg=BG_COLOR, **HIGHLIGHT_FRAME, width=720, height=300)
        self.dealer_frame.pack(side=TOP, padx=10, pady=10)
        self.dealer_frame.pack_propagate(0)

        self.dealer_cards_frame = LabelFrame(self.dealer_frame, bg=BG_COLOR, **HIGHLIGHT_FRAME, width=100, height=100)
        self.dealer_cards_frame.pack(padx=10, pady=10)

        self.name_label = Label(self.player_info_frame)
        self.name_label.pack(padx=10, pady=10
                             )
        self.chips_label = Label(self.player_info_frame)
        self.chips_label.pack(padx=10, pady=10)

        self.player_cards = Label(self.player_cards_frame, padx=5, pady=5)
        self.player_cards.pack(padx=10, pady=10)

        self.dealer_cards = Label(self.dealer_cards_frame, padx=5, pady=5)
        self.dealer_cards.pack(padx=10, pady=10)

        self.player_bet = Label(self.player_cards_frame)
        self.player_bet.pack(padx=10, pady=10)
