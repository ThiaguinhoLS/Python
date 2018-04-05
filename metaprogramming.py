# -*- coding: utf-8 -*- 

from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(x, y):
        return func(x, y)

    return wrapper

@decorator
def add(x, y):
    '''
        Add two numbers
        
    '''
    return x + y

@decorator
def sub(x, y):
    '''
        Sub two numbers
        
    '''
    return x - y



def decorator(formatter):
    '''
        Define uma forma de serem passados argumentos ao decorator, adicionando-o no seu namespace   
    '''
    def inner(func):
        '''
            Define uma função de alta ordem 
        '''    
        def wrapper(*args):
            '''
                Encapsula a função 
            '''
            print('{0:{1}}'.format(func(*args), formatter))

        return wrapper

    return inner


@decorator('.2f')
def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 0


def decorator(cls):

    original = cls.__getattribute__
    count = 1
    print(id(object.__getattribute__))
    def getattribute(self, name):
        print('getattribute')
        nonlocal count
        print('Attribute : {0}'.format(name))
        print('Intern original', id(original))
        if count < 3:
            count += 1
            return original(self, name)
        raise TypeError('Limit')

    print('Original', id(original))
    cls.__getattribute__ = getattribute
    print('Classe', id(cls.__getattribute__))
    print('getattribute', id(getattribute))

    return cls


@decorator
class Only(object):

    def __init__(self):
        self.foo = 'foo'
        self.bar = 'bar'


class Struct(object):

    _fields = []
    
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, *args):
        from itertools import zip_longest
        
        for attr, value in zip_longest(self._fields, args, fillvalue = None):
            if value is None:
                raise TypeError('Need value for attribute "{0}"'.format(attr))
            setattr(self, attr, value)


class Product(Struct):

    _fields = ['name', 'price']


product = Product('Lemon', 1.58)


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


a = product('ABCD', 'xy')
for i in a:
    print(i)
