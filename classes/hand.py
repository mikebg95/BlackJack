
class Hand(object):
    def __init__(self):
        self.cards = []

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
