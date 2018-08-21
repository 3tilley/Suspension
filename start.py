import card

def calculate_points(hand):
    #assert len(hand) == 13, "your hand needs 13 cards"
    points = 0
    for card in hand: 
        points = points + calculate_points_of_card(card)
    return points

def calculate_points_of_card(card):
    if card.rank == "A":
        return 4
    elif card.rank == "K":
        return 3
    elif card.rank == "Q":
        return 2
    elif card.rank == "J":
        return 1
    else: 
        return 0 
    
def is_balanced_hand(hand):
    singleton_or_void = 0
    for suit in card.suits:
        number_of_suit = 0
        for c in hand:
            if c.suit == suit:
                number_of_suit = number_of_suit + 1
        if number_of_suit <= 1:
            singleton_or_void = singleton_or_void + 1
    
    
    if singleton_or_void > 1:
        return False
    else:
        return True