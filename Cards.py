# Cards Module
# Basic classes for a gime with playing cards

class Card(object):
    """ A playing card. """
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.isfaceup = True

    def __str__(self):
        if self.isfaceup:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.isfaceup = not self.isfaceup

class Hand(object):
    """ A hand of playing cards."""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, perhand = 1):
        for rounds in range(perhand):
            for hand in hands:
                if self.cards:
                    topcard = self.cards[0]
                    self.give(topcard, hand)
                else:
                    print("Can't continue deal. Out of cards.")

if __name__ == "__main__":
    print("This is a module with classes for playing cards.")
    input("\nPress the enter key to exit.")
