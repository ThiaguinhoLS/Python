# -*- coding: utf-8 -*-

import collections.abc

class Power(collections.abc.Callable):

    def __call__(self, x, n):
        p = 1
        for i in range(n):
            p *= x
        return p

power = Power()


class PowerMemoization(collections.abc.Callable):

    def __init__(self):
        self.memo = {}

    def __call__(self, x, n):
        if (x, n) not in self.memo:
            if n == 0:
                self.memo[x, n] = 1
            elif n % 2 == 1:
                self.memo[x, n] = self.__call__(x, n - 1) * x
            elif n % 2 == 0:
                t = self.__call__(x, n // 2)
                self.memo[x, n] = t * t
            else:
                raise Exception('Erro lógico')
        return self.memo[x, n]


from functools import lru_cache

@lru_cache(None)
def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return power(x, n - 1) * x
    else:
        t = power(x, n // 2)
        return t * t
    

class BettingStrategy(object):

    def __init__(self):
        self.win = 0
        self.loss = 0

    def __call__(self):
        return 1

class BettingMartingale(BettingStrategy):

    def __init__(self):
        self._win = 0
        self._loss = 0
        self.stage = 1

    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, value):
        self._win = value
        self.stage = 1

    @property
    def loss(self):
        return self._loss

    @loss.setter
    def loss(self, value):
        self._loss = value
        self.stage *= 2

    def __call__(self):
        return self.stage


class BettingTwo(BettingStrategy):

    def __init__(self):
        self.win = 0
        self.loss = 0
        self.stage = 1

    def __setattr__(self, name, value):
        """ Set attributes on class """
        if name == 'win':
            self.stage = 1
        elif name == 'loss':
            self.stage *= 2
        super(BettingTwo, self).__setattr__(name, value)

    def __call__(self):
        return self.stage


import gzip
import csv


with open('subset.csv', 'w') as target:
    wtr = csv.writer(target)
    with gzip.open(path) as source:
        line_iter = (b.decode() for b in source)
        match_iter = (format_1_pat.match(line) for line in line_iter)
        wtr.writerows((m.groups() for m in match_iter if m is not None))
        
