# -*- coding: utf-8 -*-

def simple_decorator(decorator):
    def wrapper(func):
        f = decorator(func)
        f.__name__ = func.__name__
        return f
    wrapper.__name__ = decorator.__name__
    return wrapper

@simple_decorator
def decorator(func):
    def wrapper(*args, **kwargs):
        print('Called function :', func.__qualname__)
        return func(*args, **kwargs)
    return wrapper

@decorator
def grok(a, b):
    return a * b
