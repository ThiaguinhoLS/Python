# -*- coding: utf-8 -*-

class Immutable(tuple):

    def __new__(cls, a, b):
        return super(Immutable, cls).__new__(cls, (a, b))

    @property
    def a(self):
        return self[0]

    @property
    def b(self):
        return self[1]

    def __str__(self):
        return "<::: Immutable {0}, {1} :::>".format(self.a, self.b)

    def __setattr__(self, attr, value):
        raise TypeError('')

    def __delattr__(self, attr):
        raise TypeError('')


class Immutable(object):

    def __init__(self, a, b):
        super(Immutable, self).__setattr__('a', a)
        super(Immutable, self).__setattr__('b', b)

    def __setattr__(self, attr, value):
        raise AttributeError('{__class__.__name__} is Immutable'.format(__class__ = self.__class__))


from collections import namedtuple


Immutable = namedtuple("Immutable", ["a", "b"])
