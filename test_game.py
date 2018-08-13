import start
import card

def test_calculate_points():

    hand = card.cards
    pts = start.calculate_points(hand)

    assert pts == 11

def test_is_balanced_hand():
    hand = ["AS", "KS", "QS", "AH", "KH", "QH",
    "AD", "KD", "QD", "JD", "AC", "KC", "QC"]
    
    is_balanced = start.is_balanced_hand(hand)
    
    assert is_balanced == True

def test_is_unbalanced_hand():
    hand = ["AS", "KS", "QS", "JS", "10S", "9S",
    "8S", "7S", "6S", "5S", "4S", "3S", "2S"]
    
    is_balanced = start.is_balanced_hand(hand)
    
    assert is_balanced == False