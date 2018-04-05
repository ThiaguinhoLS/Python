# -*- coding: utf-8 -*-

import collections.abc

class SomeApplicationClass(collections.abc.Callable):

    def __call__(self):
        return 'Implements __call__'


def some_method(self, other):
    assert isinstance(other, collections.abc.Iterator)


from abc import ABCMeta, abstractmethod

class AbstractStrategy(metaclass = ABCMeta):

    __slots__ = ()

    @abstractmethod
    def bet(self, hand):
        return 1

    @abstractmethod
    def record_win(self, hand):
        pass

    @abstractmethod
    def record_loss(self, hand):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is Hand:
            if any('bet' in B.__dict__ for B in subclass.__mro__) and any('record_win' in B.__dict__ for B in subclass.__mro__) and \
               any('record_loss' in B.__dict__ for B in subclass.__mro__):
                return True
            return NotImplemented


class Derived(AbstractStrategy):

    def bet(self):
        pass

    def record_win(self, hand):
        pass

    def record_loss(self, hand):
        pass


derived = Derived()


class Metaclass(type):

    def __subclasscheck__(cls, subclass):
        return True if cls in subclass.__mro__ else False


class OnlyClass(metaclass = Metaclass):

    pass


class Only(OnlyClass):

    pass


class OnlyNotClass(object):

    pass

# print(issubclass(Only, OnlyClass)) >>> True
# print(issubclass(OnlyNotClass, OnlyClass)) >>> False


