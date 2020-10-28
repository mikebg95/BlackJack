# from classes.hand import Hand


class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.cards = []
        self.chips = 1000
        self.bet = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self):
        # check current score
        score = 0
        for card in self.cards:
            score += card.score

        # if more than 21, subtract 10 from first ace and return score
        while score > 21:
            for card in self.cards:
                if card.score == 11:
                    card.score -= 10
                    score -= 10
            if score > 21:
                break
        return score

    def show_cards(self, dealer=False):
        # print(self.cards[0].__repr__(True))
        if dealer:
            return [self.cards[0], self.cards[1].__repr__(True)]
        else:
            return self.cards

    # def split(self, deck):
    #     # create new list, give players second card to new hand
    #     new_hand = []
    #     new_hand.append(self.cards[1])
    #     deck.deal_top(self)
    #     new_hand.append(deck.pop(0))

