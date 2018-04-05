# -*- coding: utf-8 -*-

class Suit(object):

    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol

    def __str__(self):
        return self._symbol


Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade', '♠')


class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self.points()

    def __str__(self):
        return '{0} {1}'.format(self.rank, self.suit)


class AceCard(Card):

    def points(self):
        return 1, 11


class NumberCard(Card):

    def points(self):
        return int(self.rank), int(self.rank)


class FaceCard(Card):

    def points(self):
        return 10, 10


from itertools import product


def factory(rank, suit):

    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return  NumberCard(rank, suit)
    elif 11 <= rank < 14:
        return FaceCard({11: 'J', 12: 'Q', 13: 'K'}[rank], suit)
    else:
        raise Exception('Rank is not valid')


# cards = [factory(rank, suit) for rank, suit in product(range(1, 14), (Club, Diamond, Heart, Spade))]


def factorySemMapeamento(rank, suit):

    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(rank, suit)
    elif rank == 11:
        return FaceCard('J', suit)
    elif rank == 12:
        return FaceCard('Q', suit)
    elif rank == 13:
        return FaceCard('K', suit)
    else:
        raise Exception('Rank is not valid')


def factoryComMapeamento(rank, suit):

    type_class = {
        1: AceCard,
        11: FaceCard,
        12: FaceCard,
        13: FaceCard,
    }.get(rank, NumberCard)

    return type_class(rank, suit)


def factoryTuplasDeValores(rank, suit):

    type_class, type_rank = {
        1: (AceCard, 'A'),
        11: (FaceCard, 'J'),
        12: (FaceCard, 'Q'),
        13: (FaceCard, 'K')
    }.get(rank, (NumberCard, rank))

    return type_class(type_rank, suit)


from functools import partial


def factoryPartial(rank, suit):

    type_class = {
        1: partial(AceCard, 'A'),
        11: partial(FaceCard, 'J'),
        12: partial(FaceCard, 'Q'),
        13: partial(FaceCard, 'K')
    }.get(rank, partial(NumberCard, rank))

    return type_class(suit)


class Deck(object):

    def __init__(self):
        self._cards = [factoryPartial(rank, suit) for rank, suit in product(range(1, 14), (Club, Diamond, Heart, Spade))]

    def __str__(self):
        cards = '\n'.join(self._cards)

    
