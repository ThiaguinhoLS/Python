# -*- coding: utf-8 -*-

def debug(func):
    def wrapper(x, y):
        print(func.__qualname__)
        return func(x, y)
    return wrapper


@debug
def add(x, y):
    return x + y

# ----------------------------------------------------------------------------------------------------------------------------------

import logging

logging.basicConfig(
    filename = 'status.log',
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(funcName)s'
)

def debug(func):
    def wrapper(x, y):
        log.debug(f'Func {func.__qualname__} is called')
        return func(x, y)
    log = logging.getLogger()
    return wrapper

@debug
def add(x, y):
    return x + y


# ----------------------------------------------------------------------------------------------------------------------------------


def debug(prefix = ''):
    def decorator(func):
        message = '(' + prefix + ') ' + func.__qualname__
        def wrapper(x, y):
            print(message)
            return func(x, y)
        return wrapper
    return decorator


@debug('+')
def add(x, y):
    return x + y


# ----------------------------------------------------------------------------------------------------------------------------------

from functools import partial
def debug(func = None, *, prefix = ''):
    if func is None:
        return lambda f: debug(f, prefix = prefix)
    message = '(' + prefix + ') ' + func.__qualname__
    def wrapper(x, y):
        print(message)
        return func(x, y)
    return wrapper


@debug(prefix = '+')
def add(x, y):
    return x + y


# ----------------------------------------------------------------------------------------------------------------------------------


def debugattr(cls):

    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print('Get :', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = __getattribute__
    return cls


@debugattr
class Spam(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


# ----------------------------------------------------------------------------------------------------------------------------------


from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__qualname__)
    return wrapper

class DebugMeta(type):

    def __new__(mcs, name, bases, dct):
        clsobj = super().__new__(mcs, name, bases, dct)
        for key, val in vars(clsobj).items():
            if callable(val):
                setattr(clsobj, key, debug(val))
        return clsobj


class Spam(metaclass = DebugMeta):

    def foo(self):
        pass

    def bar(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------------------


class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Spam(Singleton):

    def __init__(self, x = None):
        self.x = x



# ----------------------------------------------------------------------------------------------------------------------------------

class Singleton(object):

    def __init__(self, klass):
        self.klass = klass
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self.klass(*args, **kwargs)
        return self._instance


@Singleton
class Spam(object):

    def __init__(self, x = None):
        self.x = x


# ----------------------------------------------------------------------------------------------------------------------------------


class Descriptor(object):

    def __init__(self, value = None):
        self.attribute = value

    def __get__(self, instance, owner):
        return self.attribute

    def __set__(self, instance, value):
        self.attribute = value

    def __delete__(self, instance):
        del self.attribute


class Spam(object):

    x = Descriptor()


# ----------------------------------------------------------------------------------------------------------------------------------


class Descriptor(object):

    def __init__(self, name = None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Spam(object):

    x = Descriptor('x')

    def __init__(self, x):
        self.x = x


# ----------------------------------------------------------------------------------------------------------------------------------


class Base(object):

    def __init__(self, x):
        self.x = x

    def foo(self):
        return self.x


class Derived(Base):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def foo(self):
        return super().foo() + self.y


# ----------------------------------------------------------------------------------------------------------------------------------


class Structure(object):

    _fields = []
    
    def __init__(self, *args):
        for key, val in zip(self._fields, args):
            setattr(self, key, val)


class Spam(Structure):

    _fields = ['x', 'y']


# ----------------------------------------------------------------------------------------------------------------------------------


def debugattr(cls):

    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print('Get :', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = __getattribute__
    return cls


class Meta(type):

    def __new__(mcs, name, bases, dct):
        clsobj = super().__new__(mcs, name, bases, dct)
        clsobj = debugattr(clsobj)
        return clsobj


class Spam(metaclass = Meta):

    def __init__(self, x):
        self.x = x


# ----------------------------------------------------------------------------------------------------------------------------------

from inspect import Parameter, Signature

def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names
    )

class Structure(object):

    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Spam(Structure):

    __signature__ = make_signature(['x', 'y'])


# ----------------------------------------------------------------------------------------------------------------------------------

from inspect import Parameter, Signature

def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names
    )

def add_signature(*names):
    def decorator(cls):
        cls.__signature__ = make_signature(names)
        return cls
    return decorator


class Structure(object):

    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


@add_signature('x', 'y')
class Spam(Structure):

    pass



# ----------------------------------------------------------------------------------------------------------------------------------


class StructMeta(type):

    def __new__(mcs, name, bases, dct):
        clsobj = super().__new__(mcs, name, bases, dct)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj


class Structure(metaclass = StructMeta):

    _fields = []
    
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return type(self).__name__ + '(' + args + ')'


class Spam(Structure):

    _fields = ['x', 'y']


# ----------------------------------------------------------------------------------------------------------------------------------



class Person(object):

    def add_property(self, attribute):
        getter = lambda self: self._get_property(attribute)
        setter = lambda self, value: self._set_property(attribute, value)
        setattr(self.__class__, attribute, property(fget = getter, fset = setter, doc = 'Auto generated'))

    def _get_property(self, attribute):
        try:
            return getattr(self, '_' + attribute)
        except AttributeError as err:
            return None

    def _set_property(self, attribute, value):
        setattr(self, '_' + attribute, value)


# ----------------------------------------------------------------------------------------------------------------------------------


class Descriptor(object):

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):

    ty = object

    def __set__(self, instance, value):
        print('typed', value)
        if not isinstance(value, self.ty):
            raise TypeError('Expected {0}'.format(self.ty))
        super().__set__(instance, value)


class Positive(Descriptor):

    def __set__(self, instance, value):
        print('positive', value)
        if value < 0:
            raise ValueError('Must be >= 0')
        super().__set__(instance, value)


class Integer(Typed):

    ty = int


class Float(Typed):

    ty = float


class String(Typed):

    ty = str


class PositiveInteger(Integer, Positive):

    'Primeiro chamará os métodos da classe Integer depois da classe Positive'

    pass


def make_signature(names):
    from inspect import Parameter, Signature
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names
    )

class StructMeta(type):

    def __new__(mcs, name, bases, dct):
        clsobj = super().__new__(mcs, name, bases, dct)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

    
class Structure(metaclass = StructMeta):

    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)
    

class Person(Structure):
    
    _fields = ['name', 'age', 'height']
    name = String('name')
    age = PositiveInteger('age')
    height = Float('height')

    
# ----------------------------------------------------------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod

class Descriptor(metaclass = ABCMeta):

    def __init__(self):
        self.attribute = None

    def __get__(self, instance, owner):
        return self.attribute

    def __set__(self, instance, value):
        if not self.validation(value):
            raise TypeError('{value} is not valid for {__class__.__name__}'.format(__class__ = self.__class__, value = value))
        self.attribute = value

    @abstractmethod
    def validation(self, value):
        pass


import re
class EmailField(Descriptor):
    
    regex = re.compile(r'\w+@\w+\.\w+')

    def validation(self, value):
        return bool(re.match(self.regex, value))


class Model(object):

    email = EmailField()


# ----------------------------------------------------------------------------------------------------------------------------------

class Descriptor(object):

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):

    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError('Expected {0.__name__}'.format(self.ty))
        super().__set__(instance, value)


class String(Typed):

    ty = str


class Integer(Typed):

    ty = int


class Float(Typed):

    ty = float
        

class Sized(Descriptor):

    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)
        
    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError('To big')
        super().__set__(instance, value)


class SizedString(String, Sized):

    pass


class Regex(Descriptor):

    def __init__(self, *args, pat, **kwargs):
        self.pat = path
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if not self.pat.match(value):
            raise ValueError('Invalid string')
        super().__set__(instance, value)














def make_signature(names):
    from inspect import Parameter, Signature
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names
    )

class StructMeta(type):

    def __new__(mcs, name, bases, dct):
        clsobj = super().__new__(mcs, name, bases, dct)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj


class Struct(metaclass = StructMeta):

    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


class Person(Struct):

    _fields = ['name', 'age', 'height']
    name = String('name')
    age = Integer('age')
    height = Float('height')
