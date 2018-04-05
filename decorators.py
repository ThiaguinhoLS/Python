# -*- coding: utf-8 -*-


def inner(name = 'bar'):
    def decorator(func):
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped
    return decorator


@inner('foo')
def foo(x):
    return x * x

def bar(x): # bar = inner('foo')(bar)
    return x * x

bar.__doc__

# -------------------------------------------------------------------------------------------------------------

from functools import wraps

trace_enable = False

def trace(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('Wrapped')
        return func(*args, **kwargs)
    return inner if trace_enable else func


@trace
def grok(x):
    return x * x


def memoize(func):
    cache = {}

    def inner(x, y):
        if (x, y) not in cache:
            cache[(x, y)] = func(x, y)
        return cache[(x, y)]

    return inner


@memoize
def foo(x, y):
    return x + y



def square(func):
    print('square')
    return lambda x: func(x * x)

def addsome(func):
    print('addsome')
    return lambda x: func(x + 42)


@square
@addsome
def identify(x):
    return x


from platform import platform

TYPES_VALUES = {'Linux': 'USER', 'Windows': 'USERNAME'}

import os


def returned_system(system):
    return TYPES_VALUES[system]

def returned_user(type_system):
    """
        Função retorna o usuário logado
    """
    system = returned_system(type_system)
    return os.environ[system]

def initialized(func):

    def inner(x):
        nonlocal initialize
        if not initialize:
            func(x)
            initialize = True

    initialize = False
    return inner


@initialized
def imprime(system):
    user = returned_user(system)
    print('Initialized a system {0}'.format(user))


imprime('Linux')
