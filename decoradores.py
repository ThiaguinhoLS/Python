# -*- coding: utf-8 -*-

def decorator(func):

    def new_func(x):
        if (x < 0):
            x = abs(x)
        func(x)

    return new_func


@decorator # func = decorator(func)
def func(x):
    print("Your number is : {x}.".format(x = x))


known = {0: 0, 1: 1}

def fibonacci(x):

    assert x >= 0, "x is not valid number"

    if (x in known): return known[x]

    res = fibonacci(x - 1) + fibonacci(x - 2)

    known[x] = res

    return res


import functools
def enhaced(method):
    @functools.wraps(method)
    def new(self, y):
        print("Enhaced method")


if (__name__ == "__main__"):
    from timeit import Timer
    t = Timer("fibonacci(100)", "from __main__ import fibonacci")
    print(t.timeit())
