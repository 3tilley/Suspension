import card
import hand

def calculate_points(hand):
    points = 0
    for card in hand.cards: 
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
        suit_count = 0
        for c in hand.cards:
            if c.suit == suit:
                suit_count += 1
        if suit_count < 2:
            singleton_or_void = singleton_or_void + 1
    
    if singleton_or_void > 1:
        return False
    else:
        return True
    
def return_longest_suit(hand):
    suits = hand.cards_by_suit()
    print(suits)
    counts = {len(v): k for k, v in suits.items()}
    longest_count = max(counts.keys())
    return counts[longest_count]

def count_longest_suit(hand, suit):
    return len([i for i in hand.cards if i.suit == suit ])

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
        
    