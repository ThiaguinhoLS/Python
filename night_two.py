# -*- coding: utf-8 -*-


import sys

def my_wraps(func):
    def inner(ffunc):
        ffunc.__name__ = func.__name__
        ffunc.__doc__ = func.__doc__
        return ffunc
    return inner

def decorator(func):
    @my_wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@decorator
def foo(x):
    '''Returns a argument'''
    return x


# ----------------------------------------------------------------------------------------------------------------------


def verify(condition, message):
    def wrapper(func):
        @my_wraps(func)
        def inner(*args, **kwargs):
            value = func(*args, **kwargs)
            if condition(value):
                return value
            raise Exception('Condition is not satisfied')
        return inner
    return wrapper


@verify(lambda x: x % 2 == 0, 'number is not valid')
def foo(x, y):
    return x / y

# -----------------------------------------------------------------------------------------------------------------------


def unique(func):
    @my_wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
    inner.called = False
    return inner

@unique
def initialize():
    print('Initialize a system')
    

# -----------------------------------------------------------------------------------------------------------------------


def count_calls(func):
    @my_wraps(func)
    def inner(*args, **kwargs):
        inner.calls += 1
        return func(*args, **kwargs)
    inner.calls = 0
    return inner

@count_calls
def mult(a, b):
    return a * b


# -----------------------------------------------------------------------------------------------------------------------


def trace(func = None, *, handle = sys.stdout):
    if func is None:
        return lambda func: trace(func, handle = handle)
    def wrapped(deco):
        @my_wraps(deco)
        def inner(*args, **kwargs):
            return deco(*args, **kwargs)
        return inner
    return wrapped


# -----------------------------------------------------------------------------------------------------------------------


def limit_calls(max_calls):
    max_calls = max_calls or float('inf')
    def wrapped(func):
        @my_wraps(func)
        def inner(*args, **kwargs):
            if not inner.calls < max_calls:
                raise Exception('Exceded calls function')
            inner.calls += 1
            return func(*args, **kwargs)
        inner.calls = 0
        return inner
    return wrapped

@limit_calls(5)
def bar(x):
    print('bar called with value :', x)


# -----------------------------------------------------------------------------------------------------------------------
