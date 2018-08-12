class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def make_card(card_str):
    suit = card_str[-1].upper()
    assert suit in "SHDC", "Invalid suit " + suit
    rank = card_str[:-1].upper()
    assert rank in "123456789JQKA" or rank == "10", "Invalid rank " + rank
    return Card(suit, rank)

cards = [make_card(c) for c in ["AS", "10H", "QD", "QC", "KC", "2D", "3D", "4D", "5D", "6D", "2C", "3C", "4C"]]
