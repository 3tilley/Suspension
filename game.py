from __future__ import print_function
import card
import hand
import start

from builtins import input
import random

def deal():
    deck = card.whole_deck.copy()
    random.shuffle(deck)
    hands = ([],[],[],[])
    card_dealt = 0
    while len(deck) > 0:
        hands[card_dealt % 4].append(deck.pop())
        card_dealt += 1

    return {"N": hand.Hand(hands[0]),
            "E": hand.Hand(hands[1]),
            "S": hand.Hand(hands[2]),
            "W": hand.Hand(hands[3])}

if __name__ == "__main__":
    print("----------------------------------------")
    print("           Suspension Bridge            ")
    print("          by Max and Charlotte          ")
    print("----------------------------------------")

    def print_hand_intro():
        inp = input("Deal a hand? [y]/n: ")
        if inp.lower() == "y" or inp == "":
            dl = deal()
            print("Your hand is:")
            h = dl["N"]
            print(h.cards_by_suit())
            print("We suggest opening:")
            opening_bid = start.opening_bid(h.cards)
            print(opening_bid)

            print_hand_intro()
    
    print_hand_intro()

