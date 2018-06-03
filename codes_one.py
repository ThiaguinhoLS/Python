# -*- coding: utf-8 -*-


class Base(object):

    def method(self):
        print('method call in class base')


class Derived(Base):

    def method(self):
        super(Derived, self).method()
        print('method call in class derived')


# ----------------------------------------------------------------------------------------------------------------------------------


def debug(func):
    from functools import wraps
    message = func.__qualname__
    @wraps(func)
    def wrapper(x, y):
        print(message)
        return func(x, y)
    return wrapper

@debug
def add(x, y):
    return x + y

@debug
def sub(x, y):
    return x - y


# ----------------------------------------------------------------------------------------------------------------------------------


class Array(object):

    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __contains__(self, item):
        return item in self.items


# ----------------------------------------------------------------------------------------------------------------------------------


def debug(func):
    import logging
    from functools import wraps
    log = logging.getLogger(func.__module__)
    message = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(message)
        return func(*args, **kwargs)
    return wrapper


# ----------------------------------------------------------------------------------------------------------------------------------


def debug(prefix = ''):
    from functools import wraps
    def decorator(func):
        message = '(' + prefix + ') ' + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@debug('+')
def add(x, y):
    return x + y

@debug('-')
def sub(x, y):
    return x - y

        
# ----------------------------------------------------------------------------------------------------------------------------------


def debug(func = None, *, prefix = ''):
    from functools import wraps, partial
    if func is None:
        return partial(debug, prefix = prefix)
    message = '(' + prefix + ') ' + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(message)
        return func(*args, **kwargs)
    return wrapper


@debug(prefix = '+')
def add(x, y):
    return x + y

@debug(prefix = '-')
def sub(x, y):
    return x - y



# ----------------------------------------------------------------------------------------------------------------------------------


def debug(prefix = ''):
    
    from functools import wraps
    def decorator(func):
        message = '(' + prefix + ') ' + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, **kwargs)
        return wrapper
        
    if callable(prefix):
        return debug()(prefix)
    return decorator

@debug('+')
def add(x, y):
    return x + y

@debug
def sub(x, y):
    return x - y


# ----------------------------------------------------------------------------------------------------------------------------------


class Spam(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def foo(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------------------


def debug(func):

    def wrapper(*args, **kwargs):
        print(func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


@debugmethods
class Spam(object):

    @classmethod
    def grok(self):
        pass

    @staticmethod
    def bar(self):
        pass

    def foo(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------------------


def debugattr(cls):
    
    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print('Get :', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = __getattribute__

    return cls


@debugattr
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


# ----------------------------------------------------------------------------------------------------------------------------------



class DebugMeta(type):

    def __new__(mcs, name, bases, dct):
        clsobj = super(DebugMeta, mcs).__new__(mcs, name, bases, dct)
        clsobj = debugmethods(clsobj)
        return clsobj


class Base(metaclass = DebugMeta):

    def foo(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------------------


class Structure(object):

    _fields = []
    def __init__(self, *args):
        for name, val in zip(self._fields, args):
            setattr(self, name, val)


class Stock(Structure):

    _fields = ['x', 'y']


# ----------------------------------------------------------------------------------------------------------------------------------


from inspect import Parameter, Signature

fields = ['name', 'shares', 'price']
parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in fields]
sig = Signature(parms)



def foo(*args, **kwargs):
    bound = sig.bind(*args, **kwargs)
    for name, val in bound.arguments.items():
        print(name, val)


print(foo(1, 2, 3))

# ---------------------------------------------------------------------------------------------------------------------------------


from inspect import Parameter, Signature


def make_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)


class Structure(object):

    __signature__ = make_signature([])
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


