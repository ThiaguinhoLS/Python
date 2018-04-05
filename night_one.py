# -*- coding: utf-8 -*-

import inspect
from contextlib import contextmanager
import doctest


class Only(object):

    pass


class OnlyClass(Only):

    pass


class ManagedFile(object):

    def __init__(self, name):
        self._name = name

    def __enter__(self):
        self.file = open(self._name, mode = 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()


@contextmanager
def enter_file(filename):

    try:
        f = open(filename, mode = 'w')
        yield f
    finally:
        f.close()


def foo(iterable):

    for i in range(len(iterable)):
        print(i)
        for j in range(0, len(iterable) - i):
            if iterable[j] > iterable[j + 1]:
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]

    print(iterable)

lista = foo([1, 4, 5, 2, 3])
    
