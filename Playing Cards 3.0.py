# Playing Cards 3.0
# Demonstrates inheritance - overriding methods

class Card(object):
    """ A playing card. """
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class UnprintableCard(Card):
    """ A Card that won't reveal its rank or suit when printed. """
    def __str__(self):
        return "<unprintable>"

class PositionableCard(Card):
    """ A Card that can be face up or face down. """
    def __init__(self, rank, suit, faceup = True):
        super(PositionableCard, self).__init__(rank, suit)
        self.isfaceup = faceup

    def __str__(self):
        if self.isfaceup:
            rep = super(PositionableCard, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.isfaceup = not self.isfaceup

# main
card1 = Card("A", "c")
card2 = UnprintableCard("A", "d")
card3 = PositionableCard("A", "h")

print("Printing an UnprintableCard object:")
print(card2)

print("\nPrinting a PositionableCard object:")
print(card3)

print("\nFlipping the PositionableCard object.")
card3.flip()

print("\nPrinting the PositionableCard object:")
print(card3)

input("\nPress the enter key to exit.")
              
    
