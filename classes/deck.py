import random


COATS = ["♠", "♥", "♦", "♣"]
NUM_CARDS = 2


# card class -> finished
class Card(object):
    def __init__(self, value, coat):
        self.value = value
        self.coat = coat
        self.score = 0

        if value == 11 or value == 12 or value == 13:
            self.score = 10
        elif value == 14:
            self.score = 11
        else:
            self.score = value

    def __repr__(self, closed=False):
        if closed:
            return "XX"
        val = ""
        if self.value == 11:
            val = "J"
        elif self.value == 12:
            val = "Q"
        elif self.value == 13:
            val = "K"
        elif self.value == 14:
            val = "A"
        else:
            val = str(self.value)
        return self.coat + val

    def show_closed(self):
        repr(self, True)


# deck class
class Deck(list):
    def __init__(self):
        super().__init__()
        self.deck = []

        # assign values and coats, shuffle
        for coat in COATS:
            for n in range(2, 15):
                self.deck.append(Card(n, coat))
        random.shuffle(self.deck)

    def top_card(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card

    def burn(self):
        self.deck.pop(0)

    # location = where card should go
    def deal_top(self, location):
        location.cards.append(self.deck.pop(0))
