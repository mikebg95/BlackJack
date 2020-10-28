from tkinter import *
from tkinter import messagebox, simpledialog
from classes.deck import Deck
from classes.player import Player
from classes.game import Game
import time
from gui.gui import Gui

# static variables
NUM_CARDS = 2
BG_COLOR = "#4a941c"
HIGHLIGHT_FRAME = {
    'highlightthickness' : 1,
    'highlightcolor' : '#FFFFFF',
    'highlightbackground' : '#FFFFFF'
}


def main():
    while True:
        gui = Gui()
        game = Game(gui)
        gui.player_bet.destroy()
        for widget in gui.player_info_frame.winfo_children():
            widget.destroy()
        new_round = messagebox.askquestion("New game?")
        if new_round == "no":
            gui.root.destroy()
            break
        else:
            gui.root.destroy()
    return


if __name__ == "__main__":
    main()
