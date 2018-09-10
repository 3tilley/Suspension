import card

class Hand():
    def __init__(self, cards):
        self.cards = cards

    def cards_by_suit(self):
        cards_dict = {
            "S": [],
            "H": [],
            "D": [],
            "C": []
        }
        for c in self.cards:
            cards_dict[c.suit].append(c)
        
        return cards_dict

    def pretty_print(self):
        w = []
        for s in card.suits:
            bitchin = self.cards_by_suit()[s] 
            wormin = f"{s}: {bitchin}"
            w.append(wormin)
        return "\n".join(w)

