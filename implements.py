# -*- coding: utf-8 -*-


# yara.lucas@novotemporh.com.br

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
    
from functools import partial

class Memoize(object):    

    def __init__(self, limit, *, message = 'Limit exceded'):
        self._limit = limit
        self._message = message

    def __call__(self, method):
        cache = {}
        count = 0

        def inner(number):
            nonlocal count
            if count < 3:
                if number not in cache:
                    cache[number] = method(number)
                count += 1
                return cache[number]
    
        inner.func = method
        return inner

@Memoize(5)                 
def fat(x):
    if x < 2:
        return 1
    return x * fat.func(x - 1)

print(fat(50))
print(fat(50))
print(fat(50))
print(fat(50))

def call(value):
    def inner(func):
        return lambda: func(value)
    return inner

@call(5)
def foo(x):
    print('Value is', x)

def call(*argv, **kwargs):
    def call_fn(fn):
         return fn(*argv, **kwargs)
    return call_fn

@call(5)
def table(n):
    value = []
    for i in range(n):
        value.append(i*i)
    return value


