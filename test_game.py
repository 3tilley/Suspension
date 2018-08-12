import start
import card

def test_calculate_points():

    hand = card.cards
    pts = start.calculate_points(hand)

    assert pts == 11