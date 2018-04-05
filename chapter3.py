# -*- coding: utf-8 -*-

import doctest


class Suit(object):

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol


Club, Diamond, Heart, Spade = Suit("Club","♣"), Suit("Diamond","♦"), Suit("Heart","♥"), Suit("Spade", "♠")


class Card(object):

    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)

    def __repr__(self):
        return "{__class__.__name__}(rank = {rank}, suit = {suit})".format(__class__ = self.__class__, **self.__dict__)


class AceCard(Card):

    """

        >>> card = AceCard(1, Club)
        >>> card
        AceCard(rank = A, suit = ♣)

    """

    def __init__(self, rank, suit):
        super(AceCard, self).__init__("A", suit, 1, 11)


class NumberCard(Card):

    """

        >>> card = NumberCard(2, Club)
        >>> card
        NumberCard(rank = 2, suit = ♣)

    """

    def __init__(self, rank, suit):
        super(NumberCard, self).__init__(rank, suit, int(rank), int(rank))


class FaceCard(Card):

    """

        >>> card = FaceCard(11, Club)
        >>> card
        FaceCard(rank = J, suit = ♣)

    """

    def __init__(self, rank, suit):
        super(FaceCard, self).__init__({11: "J", 12: "Q", 13: "K"}[rank], suit, 10, 10)


def card(rank, suit):
    if (rank == 1):
        return AceCard(rank, suit)
    elif (2 <= rank < 11):
        return NumberCard(rank, suit)
    elif (11 <= rank < 14):
        return FaceCard(rank, suit)
    else:
        raise ValueError("Rank is not number valid")


class Generic(object):

    def __getattr__(self, attr):
        return "Generic no contains attribute {0}".format(attr)


class Hand(object):

    def __str__(self):
        return ', '.join(map(str, self.card))

    def __repr__(self):
        return '{__class__.__name__}({dealer_card}, {cards}'.format(__class__ = self.__class__, \
                                                                    cards = self._cards, dealer_card = self._dealer_card)



class HandLazy(Hand):

    def __init__(self, dealer_card, *cards):
        self._dealer_card = dealer_card
        self._cards = list(cards)

    @property
    def total(self):
        delta = max(card.soft - card.hard for card in self._cards)
        hard_total = sum(card.hard for card in self._cards)
        if hard_total + delta_soft <= 21:
            return hard_total + delta
        return hard_total

    @property
    def card(self):
        return self._cards

    @card.setter
    def card(self, other_card):
        self._cards.append(other_card)

    @card.deleter
    def card(self):
        self._cards.pop(-1)


class HandEager(Hand):

    def __init__(self, dealer_card, *cards):
        self._dealer_card = dealer_card
        self.total = 0
        self._delta_soft = 0
        self._hard_total = 0
        self._cards = list()
        for card in cards:
            self.card = card

    @property
    def card(self):
        return self._cards

    @card.setter
    def card(self, other_card):
        self._cards.append(other_card)
        self._delta_soft = max(other_card.soft - other_card.hard, self._delta_soft)
        self._hard_total += other_card.hard
        self._set_total()

    @card.deleter
    def card(self):
        removed = self._cards.pop(-1)
        self._hard_total -= removed.hard
        self._delta_soft = max(card.soft - card.hard for card in self._card)
        self._set_total()

    def _set_total(self):
        if self._hard_total + self._delta_soft <= 21:
            self.total = self._hard_total + self._delta_soft

    def split(self, deck):
        assert self._cards[0].rank == self._cards[1].rank
        self.card = deck.pop()
        card = self._cards[-1]
        del self.card
        new_hand = self.__class__(self._dealer_card, card, deck.pop())


class CardImmutable(object):

    __slots__ = ('rank', 'suit', 'hard', 'soft')

    def __init__(self, rank, suit, hard, soft):
        super(CardImmutable, self).__setattr__('rank', rank)
        super(CardImmutable, self).__setattr__('suit', suit)
        super(CardImmutable, self).__setattr__('hard', hard)
        super(CardImmutable, self).__setattr__('soft', soft)

    def __str__(self):
        return '{0.rank}{0.suit}'.format(self)

    def __setattr__(self, name, value):
        raise AttributeError('{__class__.__name__} has no attribute "{name}"'.format(__class__ = self.__class__, name = name))



class CardTuple(tuple):

    def __new__(cls, rank, suit, hard, soft):
        return tuple.__new__(cls, (rank, suit, hard, soft))

    def __getattr__(self, value):
        return self[{'rank': 0, 'suit': 1, 'hard': 2, 'soft': 3}[value]]

    def _setattr__(self, name, value):
        raise AttributeError('Error class is immutable')


class RateTimeDistance(dict):

    def __init__(self, *args, **kwargs):
        super(RateTimeDistance, self).__init__(*args, **kwargs)
        self._solve()

    def __getattr__(self, name):
        return self.get(name, None)

    def __setattr__(self, name, value):
        self[name] = value
        self._solve()

    def __dir__(self):
        return list(self.keys())

    def _solve(self):
        if self.rate is not None and self.time is not None:
            self['distance'] = self.rate * self.time
        elif self.rate is not None and self.distance is not None:
            self['time'] = self.distance / self.rate
        elif self.time is not None and self.distance is not None:
            self['rate'] = self.distance / self.time

r = RateTimeDistance(rate = 10, time = 2)
print(dir(r))
print('Rate = {rate}, Time = {time}, Distance = {distance}'.format(**r))


class BlackjackCard3(object):

    def __init__(self, rank, suit, hard, soft):
        super(BlackjackCard3, self).__setattr__('rank', rank)
        super(BlackjackCard3, self).__setattr__('suit', suit)
        super(BlackjackCard3, self).__setattr__('hard', hard)
        super(BlackjackCard3, self).__setattr__('soft', soft)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Can"t not set "{name}" in instance'.format(name= name))
        raise AttributeError('{__class__.__name__} has no attribute "{name}"'.format(__class__ = self.__class__, name = name))

    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError('Attibute private')
        return super(BlackjackCard3, self).__getattribute__(name)


class Foo(object):

    def addProperty(self, attribute):
        getter = lambda self: self._getProperty(attribute)
        setter = lambda self, value: self._setProperty(attribute, value)
        setattr(self.__class__, attribute, property(fget = getter, fset = setter, doc = 'Auto gerado'))

    def _getProperty(self, attribute):
        print('_getProperty')
        return getattr(self, '_' + attribute)

    def _setProperty(self, attribute, value):
        print('_setProperty')
        setattr(self, '_' + attribute, value)


class UnityValue(object):

    def __init__(self, unit):
        self.value = None
        self.unit = unit
        self.default_format = '.2f'

    def __set__(self, instance, value):
        self.value = value

    def __str__(self):
        return '{value:{spec}} {unit}'.format(spec = self.default_format, **self.__dict__)

    def __format__(self, spec = ' '):
        """

            Deve-se converter para strings pois object.__format__ não permite formatação gerando um exceção TypeError

        """
        if spec == ' ':
            spec = self.default_format
        return '{value!s:{spec}} {unit}'.format(spec = spec, value = self.value, unit = self.unit)


class RTD(object):

    rate = UnityValue('KT')
    time = UnityValue('HR')
    distance = UnityValue('NM')

    def __init__(self, rate = None, time = None, distance = None):
        if rate is None:
            self.time = time
            self.distance = distance
            self.rate = distance / time
        if time is None:
            self.rate = rate
            self.distance = distance
            self.time = distance / rate
        if distance is None:
            self.rate = rate
            self.time = time
            self.distance = rate * time

    def __str__(self):
        return 'rate: {0.rate} time = {0.time} distance = {0.distance}'.format(self)


#instance = RTD(rate = 10, distance = 2)
#print(str(instance))


class Unit(object):

    conversion = 1.0

    def __get__(self, instance, owner):
        return instance.kph * self.conversion

    def __set__(self, instance, value):
        instance._kph = value / self.conversion

    
class Knots(Unit):

    conversion = 0.5399568


class MPH(Unit):

    conversion = 0.62137117


class KPH(Unit):

    def __get__(self, instance, owner):
        print('KPH __get__')
        return instance._kph

    def __set__(self, instance, value):
        print('KPH __set__')
        instance._kph = value


class Measurement(object):

    kph = KPH()
    knots = Knots()
    mph = MPH()

    def __init__(self, kph = None, knots = None, mph = None):
        if kph is not None:
            self.kph = kph
        elif knots is not None:
            self.knots = knots
        elif mph is not None:
            self.mph = mph
        else:
            raise TypeError('')

    def __str__(self):
        return 'rate : {0.kph}kph = {0.knots}knots = {0.mph}mph'.format(self)
    

a = Measurement(knots = 2)
