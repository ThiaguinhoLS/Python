# -*- coding: utf-8 -*-


def memoize(func):

    cache = {}

    def wrapped(number):
        if number not in cache:
            cache[number] = func(number)
        return cache[number]

    return wrapped


class Memoize(object):

    def __init__(self, method):
        self._method = method
        self._cache = {}

    def __call__(self, number):
        if number not in self._cache:
            self._cache[number] = self._method(number)
        return self._cache[number]



def memoize(limit, *, message = 'Limit exceded'):
    count = 0
    
    def inner(func):
        cache = {}
        
        def wrapped(number):
            nonlocal count
            if count < limit:
                if number not in cache:
                    cache[number] = func(number)
                count += 1
                return cache[number]
            print(message, count)
            
        wrapped.func = func

        return wrapped

    return inner
    

@memoize(5)
def fat(x):
    if x < 2:
        return 1
    return x * fat.func(x - 1)

