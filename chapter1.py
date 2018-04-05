# -*- coding: utf-8 -*-

import doctest

class Suit(object):

    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol

    def __str__(self):
        return self._symbol


Club, Diamond, Heart, Spade = Suit("Club","♣"), Suit("Diamond","♦"), Suit("Heart","♥"), Suit("Spade", "♠")


class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)

    def __repr__(self):
        return "{__class__.__name__}(rank = {rank}, suit = {suit})".format(__class__ = self.__class__, **self.__dict__)


class AceCard(Card):

    def _points(self):
        return 1, 10


class NumberCard(Card):

    def _points(self):
        return int(rank), int(rank)


class FaceCard(Card):


    def _points(self):
        return 10, 10


def card(rank, suit):
    if (rank == 1):
        return AceCard("A", suit)
    elif (2 <= rank < 11):
        return NumberCard(rank, suit)
    elif (11 <= rank < 14):
        _rank = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(_rank, suit)
    else:
        raise ValueError("Rank is not valid")



def card(rank, suit):
    if (rank == 1):
        return AceCard("A", suit)
    elif (2 <= rank < 11):
        return NumberCard(rank, suit)
    elif (rank == 11):
        return FaceCard("J", suit)
    elif (rank == 12):
        return FaceCard("Q", suit)
    elif (rank == 13):
        return FaceCard("K", suit)
    else:
        raise ValueError("Rank is not valid")



def card(rank, suit):
    _rank = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(rank, rank)
    _class = {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
    return _class(rank, suit)


from functools import partial


def card(rank, suit):
    part_class = {
        1: partial(AceCard, "A"),
        11: partial(FaceCard, "J"),
        12: partial(FaceCard, "Q"),
        13: partial(FaceCard, "K")
    }.get(rank, partial(NumberCard, rank))
    return part_class(suit)


class FluentAPI(object):

    def rank(self, rank):
        self._class, self._rank = {
            1: (AceCard, "A"),
            11: (FaceCard, "J"),
            12: (FaceCard, "Q"),
            13: (FaceCard, "K")
        }.get(rank, (NumberCard, rank))
        return self

    def suit(self, suit):
        return self._class(self._rank, suit)


class CardImutable(object):

    __slots__ = ("rank", "suit", "hard", "soft")

    def __init__(self, rank, suit, hard, soft):
        super().__setattr__("rank", rank)
        super().__setattr__("suit", suit)
        super().__setattr__("hard", hard)
        super().__setattr__("soft", soft)

    def __setattr__(self, attr, value):
        raise AttributeError("{__class__.__name__} has no attribute '{attr}'".format(__class__ = self.__class__, attr = attr))


    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)



class CardTuple(tuple):

    def __new__(cls, rank, suit, hard, soft):
        return super(CardTuple, cls).__new__(cls, (rank, suit, hard, soft))

    def __getattr__(self, attr):
        return self[{"rank": 0, "suit": 1, "hard": 2, "soft": 3}[attr]]

    def __setattr__(self, attr, value):
        raise AttributeError('Immutable')


card = CardTuple("A", Club, 1, 11)
    
    
        
