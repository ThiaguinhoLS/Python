# -*- coding: utf-8 -*-

# Decorators implements

'''

Temos muitas funções que possuem corpos de função parecidos

'''

def decorator(name):
    def wrapper(function):
        def inner(a, b):
            print(f'Executing {name} ...')
            print(function(a, b))
        return inner
    return wrapper
        

@decorator(name = 'Adição')
def add(x, y):
    return x + y

@decorator(name = 'Subtração')
def sub(x, y):
    return x - y

'''

Esse decorator resolve um dos problemas ao implementar o decoradores nos códigos que é a perda do nome da função, e sua documentação,
pois muitas vezes retornamos uma função que encapsula a função passada.

'''


def wraps(function):
    def wrapper(decorated):
        decorated.__name__ = function.__name__
        decorated.__doc__ = function.__doc__
        return decorated
    return wrapper

def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

@decorator
def square(x):
    'Returns as square of number passed of argument'
    return x * x

'''

Faz com que os decoradores não percam dados das funções que os mesmos decoram


'''

def envolved(decorator):
    def wrapper(deco):
        f = decorator(deco)
        f.__name__ = deco.__name__
        f.__doc__ = deco.__doc__
        f.__dict__.update(deco.__dict__)
        return f
    wrapper.__name__ = decorator.__name__
    wrapper.__doc__ = decorator.__doc__
    wrapper.__dict__.update(decorator.__dict__)
    return wrapper

@envolved
def decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

@decorator
def square(x):
    'Square function'
    return x * x

'''

Decorator que memoriza as entradas e retorna a saída caso a mesma já tenha sido armazenada por uma chamada anterior, ou armazena e
retorna a mesma.

'''


def memoize(function):
    cache = {}
    @wraps(function)
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.keys()))
        if key not in cache:
            value = function(*args, **kwargs)
            cache[key] = value
        return cache[key]
    return wrapper

@memoize
def fat(x):
    for i in range(1, x):
        x *= i
    return x


'''

Decorator que só executa uma única vez a função decorada

'''


def one_initialize(function):
    def wrapper(*args, **kwargs):
        nonlocal initialize
        if not initialize:
            function(*args, **kwargs)
            initialize = True
    initialize = False
    return wrapper

@one_initialize
def initialize_system():
    print('Initialized system')


'''

Decorador implementa o padrão de projeto singleton que viabiliza que o script só possa criar uma instância de determinada classe

'''


def singleton(klass):
    instance = None
    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = klass(*args, **kwargs)
        return instance
    return wrapper



'''

Decorador que imprime o tempo de execução da função decorada

'''


def timer(function):
    from time import time
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time()
        function(*args, **kwargs)
        print('Time of the executing : {0}'.format(time() - start))
    return wrapper

@timer
def fat(x):
    for i in range(1, x):
        x *= i
    return x


'''

Decorador cria uma função de despache único

'''

class singledispatch(object):

    def __init__(self, function):
        self._function = function
        self._types = {}

    def __call__(self, arg):
        if type(arg) not in self._types:
            return self._function(arg)
        return self._types[type(arg)](arg)

    def register(self, type):
        def _wrapper(function):
            self._types.update({type: function})
        return _wrapper


def singledispatch(function):
    
    types = {}
    def wrapper(arg):
        if type(arg) not in types:
            return function(arg)
        return types[type(arg)](arg)
    
    def register(type):
        def wrapper(function):
            types.update({type: function})
        return wrapper

    wrapper.register = register
    return wrapper
    
 

# -----------------------------------------------------------------------------------------------------------------------------------

# Gerenciadores de contexto

'''

Classe que implementa o protocolo de gerenciamento de contexto, por meio dos métodos especiais '__enter__', '__exit__'

'''

class ManagedFile(object):

    def __init__(self, filename, mode = 'w'):
        from functools import partial
        self._opener = partial(open, filename, mode)

    def __enter__(self):
        self._handle = self._opener()
        return self._handle

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._handle.close()
        del self._handle


'''

Utilizando o decorador contextmanager para implementar um gerenciador de contexto

'''

from contextlib import contextmanager

@contextmanager
def change_path(path):
    import os
    actual = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(actual)


# -----------------------------------------------------------------------------------------------------------------------------------

# Padrões de projeto


'''

Padrão de projeto singleton permite a criação de somente uma instância da classe

'''

class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance


'''

Padrão MVC que ajuda a separar a lógica do código

'''

class Model(object):

    def __init__(self):
        self.options = (
            ('Adição', self.add),
            ('Subtração', self.sub),
        )

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

class View(object):

    def show(self, options):
        print('[0] - Sair')
        for number, option in enumerate(options, 1):
            print(f'[{number}] - {option[0]}')

    def values(self):
        values = []
        while len(values) < 2:
            try:
                value = input('Enter as value : ')
                value = int(value)
            except ValueError as err:
                pass
            else:
                values.append(value)
        return values
            
    def execute(self, options):
        while True:
            self.show(options)
            option = int(input('Choose a option : '))
            if 0 <= option <= len(options):
                if option == 0:
                    break
                a, b = self.values()
                print(options[option - 1][1](a, b))
    

class Controller(object):

    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        self.view.execute(self.model.options)


def main():
    controller = Controller()
    controller.run()

'''

Definindo uma classe imutável com o uso de slots

'''

class Card(object):

    __slots__  = ('rank', 'suit')

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{rank} {suit}'.format(rank = self.rank, suit = self.suit)

    def __repr__(self):
        return '{__class__.__name__}(rank = {0}, suit = {1})'.format(self.rank, self.suit, __class__ = self.__class__)

'''

Definindo uma classe imutável herdando de uma tupla

'''

class Card(tuple):

    def __new__(self, rank, suit):
        return tuple.__new__(self, (rank, suit))

    def __getattr__(self, attr):
        if attr == 'rank':
            return self[0]
        elif attr == 'suit':
            return self[1]
        raise AttributeError('{__class__.__name__} as not attribute "{attr}"'.format(__class__ = self.__class__, attr = attr))

    def __setattr__(self, attr, value):
        if attr == 'rank':
            self[0] = value
        elif attr == 'suit':
            self[1] = value
        else:
            raise AttributeError('{__class__.__name__} as not permit assigment'.format(__class__ = self.__class__, attr = attr))

'''


'''


class Singleton(object):

    _instance = None

    def get(self):
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance
        
    def __init__(self):
        if Singleton._instance is not None:
            raise Exception('Singleton class has instanced')
        Singleton._instance = self


'''


'''


class Definitions(object):

    def __init__(self, *args):
        try:
            for field, attr in zip(self._fields, args):
                setattr(self, field, attr)
        except AttributeError as err:
            pass

    def __setattr__(self, attr, value):
        if hasattr(self, '_fields'):
            if attr not in self._fields:
                raise AttributeError(f'Attribute "{attr}" not found')
        self.__dict__[attr] = value
            
class Define(Definitions):

    _fields = ['name', 'value']
    

'''


'''


class Singleton(object):

    def __init__(self, klass):
        self._klass = klass

    def __call__(self, *args, **kwargs):
        if not hasattr(self, '_instance'):
            self._instance = self._klass(*args, **kwargs)
        return self._instance


'''



'''

def send(method):
    def wrapper(self, *args):
        args = list(args)
        args[0] = '_' + args[0]
        return method(self, *args)
    return wrapper

class Property(object):

    def add_property(self, attribute):
        getter = lambda self: self._get(attribute)
        setter = lambda self, value: self._set(attribute, value)
        deletter = lambda self: self._del(attribute)
        setattr(self.__class__, attribute, property(fget = getter, fset = setter, fdel = deletter, doc = 'Auto generated'))

    @send
    def _get(self, attribute):
        print('Getting {0}'.format(attribute))
        return getattr(self, attribute)

    @send
    def _set(self, attribute, value):
        print('Setting {0}'.format(attribute))
        setattr(self, attribute, value)

    @send
    def _del(self, attribute):
        print('Deletting {0}'.format(attribute))
        del self.__dict__[attribute]


p = Property()
p.add_property('name')

