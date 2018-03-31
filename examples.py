# -*- coding: utf-8 -*-

class Base(object):

    def foo(self):
        return self.bar()


class Derived(Base):

    def bar(self):
        return 'bar'

# -------------------------------------------------------------------------------------------------------------

class Only(object):

    def __new__(cls, *args, **kwargs):
        obj = super(Only, cls).__new__(cls)
        obj.name = cls.__name__
        return obj

class OnlyDerived(Only):

    def __init__(self):
        self.name = 'Object'


# -------------------------------------------------------------------------------------------------------------

from collections import OrderedDict

class MetaClass(type):

    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()

    def __new__(mcs, name, bases, namespace):
        return super(MetaClass, mcs).__new__(mcs, name, bases, namespace)


class Default(object, metaclass = MetaClass):

    name = 'Default'
    value = 'Subclass'

    def __init__(self):
        """ Initialize the object value in attributes """
        self.x = 'X'
        self.y = 'Y'

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'

# -------------------------------------------------------------------------------------------------------------

import os.path

def verify_exists(method):
    
    def new_func(self):
        if os.path.exists(self.filename):
            self.filename = self.filename + '(1)'
        return method(self)
    
    return new_func

class ManagedFile(object):

    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return 'Created filename is {0}'.format(self.filename)

    @verify_exists
    def __enter__(self):
        self.file = open(self.filename, mode = 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()

#with ManagedFile('hello.txt') as f:
#    f.write('Hello World\n')

# -------------------------------------------------------------------------------------------------------------

"""

 Implements pattern MVC


"""

import sys

class Model(object):

    def __init__(self):
        self.data = (
            'Os homens erram, os grandes assumem que erraram',
            'Quando a discussão é longa ambas as partes estão erradas'
        )

    def get_data(self, index):
        try:
            return self.data[index - 1]
        except IndexError as error:
            return 'Number of index is not valid'


class View(object):

    def show(self, word):
        print(word)


def valida_number():
    try:
        value = input('Enter as number of word : ')
        value = int(value)
    except ValueError:
        value = 0
    return value
        

class Controller(object):

    def __init__(self):
        self.view = View()
        self.model = Model()

    def play(self):
        while True:
            index = valida_number()
            if index == 'quit':
                sys.exit(0)
            word = self.model.get_data(index)
            self.view.show(word)

# -------------------------------------------------------------------------------------------------------------


"""

Implements pattern Observer


"""

class Subject(object):

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            print('<::: Error from removed ... :::>')

    def notify(self):
        [observer.show(self) for observer in self._observers]


class Formatter(object):

    def show(self, value : int):
        raise NotImplementedError


class DefaultFormatter(Subject):

    def __init__(self, data):
        super(DefaultFormatter, self).__init__()
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        try:
            value = int(value)
            print(value)
            self.notify()
        except ValueError:
            print('<::: Data is not valid :::>')


class BinaryFormatter(object):

    def show(self, other):
        print('Value is altered for : ', bin(other.data))


class HexFormatter(object):

    def show(self, other):
        print('Value is altered for : ', hex(other.data))
        
"""

if __name__ == '__main__':
    default = DefaultFormatter(20)
    binary = BinaryFormatter()
    hexadecimal = HexFormatter()
    default.add_observer(binary)
    default.data = 10
    default.add_observer(hexadecimal)
    default.data = 5

"""

# -------------------------------------------------------------------------------------------------------------


"""

Implements pattern Strategy


"""


class Strategy(object):

    def method(self, value):
        raise NotImplementedError


class ConcretStrategyA(Strategy):

    def method(self, value):
        print(__class__.__name__)
        print('Value is', value * 2)


class ConcretStrategyB(Strategy):

    def method(self, value):
        print(__class__.__name__)
        print('Value is', value * 5)


class Only(object):

    def __init__(self, strategy = None):
        if strategy is not None:
            self.strategy = strategy.method

    def strategy(self, value):
        print(__class__.__name__)
        print('Value is', value)

"""

strategyA = ConcretStrategyA()
strategyB = ConcretStrategyB()
onlyA = Only(strategyA)
onlyB = Only(strategyB)
onlyC = Only()
[obj.strategy(1) for obj in (onlyA, onlyB, onlyC)]

"""
        
# -------------------------------------------------------------------------------------------------------------


"""

Implements pattern iterator


"""

class Iterable(object):

    def __init__(self, value, max_value):
        self._value = value
        self._max_value = max_value

    def __next__(self):
        value = self._value
        if self._value >= self._max_value:
            raise StopIteration
        self._value += 1
        return value

    def __iter__(self):
        return self
    
"""

for i in Iterable(1, 4):
    print(i)
    
"""

class ImplementsIterable(object):

    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def __iter__(self):
        return ConcretIterable(self._min_value, self._max_value)


class ConcretIterable(object):

    def __init__(self, value, max_value):
        self._value = value
        self._max_value = max_value

    def __next__(self):
        value = self._value
        if value >= self._max_value:
            raise StopIteration
        self._value += 1
        return value

"""

for i in ImplementsIterable(1, 5):
    print(i)


"""

# -------------------------------------------------------------------------------------------------------------

"""

Implements pattern factory method


"""

class Transport(object):

    @staticmethod
    def method_get(type_transport : str):
        if type_transport == 'car':
            return Car()
        elif type_transport == 'airplane':
            return Airplane()
        else:
            raise TypeError('Type of transport not is valid')


class Car(object):

    def __str__(self):                                                                                          
        return 'Car'
                                                                                                                                                                                                                                                                                    
                        
class Airplane(object):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

    def __str__(self):
        return 'Airplane'

"""

transport = Transport()
values = [transport.method_get(value) for value in ('car', 'airplane')]
[print(obj) for obj in values]


"""

# -------------------------------------------------------------------------------------------------------------


"""

Implements pattern decorator

"""


def decorator(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.__doc__ = func.__doc__

    return wrapper


@decorator
def foo(x):
    """

    function foo
    
    """
    return x * x



from functools import wraps

def extended(func):

    @wraps(func)
    def wrapper(x):
        return func(x)

    return wrapper    

@extended
def bar(x):
    """

    function bar

    """

    return x ** 2



class Wrapper(object):

    def __init__(self, method):
        self._method = method
        self._cache = {}

    def __call__(self, number):
        try:
            value = self._cache[number]
        except KeyError as error:
            value = self._method(number)
            self._cache[number] = value
        return value

@Wrapper
def fatorial(number):

    if number < 2:
        return 1
    return number * fatorial(number - 1)

"""

from time import time

initial = time()
value = fatorial(50)
final = time()
print('Time is function : ', final - initial)


"""

# -------------------------------------------------------------------------------------------------------------


"""

Implements pattern Proxy


"""

class SGBD(object):

    def __init__(self):
        self._users = ['bill', 'pool', 'michael']

    def add_user(self, user):
        if user not in self._users:
            self._users.append(user)
        else:
            print('<::: Desculpe o usuário já está adicionado :::>')

    @property
    def user(self):
        return self._users


class Proxy(object):

    def __init__(self):
        self._model = SGBD()
        self._password = '1230'

    def add_user(self, user):
        password = input('Enter as password : ')
        if password == self._password:
            self._model.add_user(user)
        else:
            print('Password is not valid')

    def view_users(self):
        users = ' '.join(self._model.user)
        print('Usuários :', users)
        

class Main(object):

    def __init__(self):
        self.proxy = Proxy()

    def play(self):
        while True:
            option = input('[1] - Para Adicionar usuário / [2] - Visualizar usuários : / [0] - Sair :')
            if option == '0':
                sys.exit(0)
            elif option == '1':
                user = input('What your name ?: ')
                self.proxy.add_user(user)
            elif option == '2':
                self.proxy.view_users()
            else:
                print('<::: Option is not valid :::>')

# -------------------------------------------------------------------------------------------------------------
                
        
"""

Implements pattern facade

"""


class Memory(object):

    def run(self):
        print('Initialized memory is computer')


class HD(object):

    def play(self):
        print('Initialized HD is computer')


class Computer(object):

    def __init__(self):
        self.memory = Memory()
        self.hd = HD()

    def initialize(self):
        self.memory.run()
        self.hd.play()

"""

if __name__ == '__main__':
    computer = Computer()
    computer.initialize()

"""
# -------------------------------------------------------------------------------------------------------------

"""

implements pattern Singleton

"""


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Only(Singleton):

    def __init__(self):
        self.x = 'X'
        self.y = 'Y'


class SingletonWrapped(object):

    def __init__(self, instance):
        self._instance = instance

    def __call__(self, *args, **kwargs):
        try:
            return self._only
        except AttributeError as error:
            self._only = self._instance(*args, **kwargs)
            return self._only

@SingletonWrapped
class Unique(object):

    def __init__(self, value):
        self.value = value

if __name__ == '__main__':
    a = Unique('A')
    b = Unique('B')
    print(a.value)
    assert a is b
