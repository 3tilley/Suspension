import start
import card

def test_calculate_points():

    hand = card.cards
    pts = start.calculate_points(hand)

    assert pts == 11

def test_is_balanced_hand():
    balanced_cards = ["AS", "KS", "QS", "AH", "KH", "QH",
    "AD", "KD", "QD", "JD", "AC", "KC", "QC"]
    hand = [card.make_card(c) for c in balanced_cards]
    is_balanced = start.is_balanced_hand(hand)
    assert is_balanced == True

def test_is_unbalanced_hand():
    unbalanced_cards = ["AS", "KS", "QS", "JS", "10S", "9S",
    "8S", "7S", "6S", "5S", "4S", "3S", "2S"]
    
    hand = [card.make_card(c) for c in unbalanced_cards]
    
    is_balanced = start.is_balanced_hand(hand)
    
    assert is_balanced == False