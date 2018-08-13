from card import cards

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
    
hand = cards
calculate_points(hand)


