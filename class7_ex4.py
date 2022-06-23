import random


class Card:

    def __init__(self, rank, suit):  # initializer/constructor
        self.rank = rank
        self.suit = suit

    def __str__(self):  # returns a string representation of the object
        return "(" + self.rank + "," + self.suit + ")"

    def get_rank(self):  # accessor/getter
        return self.rank

    def get_rank_as_int(self):
        big_ranks = {'A': 11, 'K': 10, 'Q': 10, 'J': 10}
        if self.rank in big_ranks:
            return big_ranks[self.rank]
        else:
            return int(self.rank)

    def get_suit(self):
        return self.suit

    def set_rank(self, new_rank):  # mutator/setter
        self.rank = new_rank

    def set_suit(self, new_suit):
        self.suit = new_suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in ['H', 'D', 'S', 'C']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                new_card = Card(rank, suit)
                self.deck.append(new_card)

    def __str__(self):
        result = ""
        for item in self.deck:
            result += str(item) + " "
        return result

    def shuffle(self):
        new_deck = []
        while len(self.deck) > 0:
            rnd_index = random.randint(0, len(self.deck)-1)
            new_deck.append(self.deck[rnd_index])
            del self.deck[rnd_index]

        self.deck = new_deck

    def deal_a_card(self):
        return self.deck.pop(0)


def main():
    red_deck = Deck()

    print(red_deck, end="\n \n")

    red_deck.shuffle()
    print(red_deck, end="\n \n")

    for _ in range(3):  # use an underscore if you don't plan on using the variable at all
        card = red_deck.deal_a_card()

        card_int = card.get_rank_as_int()

        print(card_int)


if __name__ == "__main__":
    main()