# building a card class
# classes have attributes and behaviors
# self allows us to refer to the object we are working on

class Card:

    def __init__(self, rank, suit):  # initializer/constructor
        self.rank = rank
        self.suit = suit

    def __str__(self):  # returns a string representation of the object
        return self.rank + " " + self.suit

    def get_rank(self):  # accessor/getter
        return self.rank

    def get_suit(self):
        return self.suit

    def set_rank(self, new_rank):  # mutator/setter
        self.rank = new_rank

    def set_suit(self, new_suit):
        self.suit = new_suit


def main():
    card_one = Card('K', 'D')
    card_two = Card('6', 'C')

    print("Card one's rank is:", card_one.get_rank())
    print("Card one's suit is:", card_one.get_suit(), end='\n \n')

    card_one.set_rank('4')
    card_one.set_suit('S')
    print("Card one's new rank is:", card_one.get_rank())
    print("Card one's new suit is:", card_one.get_suit(), end='\n \n')

    print("Card two's rank is:", card_two.get_rank())
    print("Card two's suit is:", card_two.get_suit(), end='\n \n')

    print("Card one str:", card_one.__str__())  # stupid so don't use it
    print("Card two str:", card_two, end='\n \n')  # <---- use this instead


if __name__ == "__main__":
    main()
