import start
import card
import hand


balanced_cards = ["AS", "KS", "QS", "AH", "KH", "QH",
    "AD", "KD", "QD", "JD", "AC", "KC", "QC"]

balanced_hand = hand.Hand([card.make_card(c) for c in balanced_cards])

unbalanced_cards = ["AS", "KS", "QS", "JS", "10S", "9S",
    "8S", "7S", "6S", "5S", "4S", "3S", "2S"]

unbalanced_hand = hand.Hand([card.make_card(c) for c in unbalanced_cards])

def test_calculate_points():

    hand = card.cards
    pts = start.calculate_points(hand)

    assert pts == 11

def test_is_balanced_hand():
    is_balanced = start.is_balanced_hand(balanced_hand)
    assert is_balanced == True

def test_is_unbalanced_hand():    
    is_balanced = start.is_balanced_hand(unbalanced_hand)
    assert is_balanced == False

def test_hand_pretty_print():
    test_hand = balanced_hand
    #print(test_hand.pretty_print())
    test_hand.pretty_print()