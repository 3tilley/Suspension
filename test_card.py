import card

def test_card():
    c = card.make_card("10D")
    assert c.suit == "D"
    assert c.rank == "10"
