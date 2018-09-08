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
        suit = 0
    for c in hand:
        if c.suit == suit:
            singleton_or_void = singleton_or_void + 1
    
    if singleton_or_void > 1:
        return False
    else:
        return True
    
def return_longest_suit(hand):
    return "S"

def count_longest_suit(hand, suit):
    return len([i for i in hand if i.Suit == suit ])

def opening_bid(hand):
    points = calculate_points(hand)
    if is_balanced_hand(hand):
        if points < 12:
            return "pass"
        elif 12 <= points <= 14:
            return "1" + return_longest_suit(hand)
        elif 18 <= points <= 19:
            return "1NT"
        elif 20 <= points <= 21:
            return "2NT"
    else:
        if (5 <= points <= 10):
            s = return_longest_suit(hand)
            if count_longest_suit(hand, s) > 5:
                return "2" + s
        else:
            return "pass"
        
    