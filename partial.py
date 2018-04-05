# -*- coding: utf-8 -*-

from functools import partial
import doctest


def _partial(func):

    """Partial implementation"""
    pass


class Partial(object):

    def __init__(self, function):
        self._function = function
        self._cache = dict()

    def __call__(self, *args):
        try:
            return self._cache[args]
        except KeyError as error:
            result = self._function(*args)
            self._cache[args] = result
            return result


@Partial
def mult(x, y):

    """Multiply two numbers"""

    return x * y


def _partial(function):

    def new_func(*args):

        return func(*args)

    return new_func


@_partial
def sub(x, y):
    return x - y


def login_required(user):

    def new_func(function):

        def proxy():

            if (user is not None):
                return function()
            else:
                raise Exception("Error")

        return proxy

    return new_func


@login_required()




if (__name__ == "__main__"):
    print(mult(2, 5))
    print(mult(2, 7))
    print(mult(2, 5))
