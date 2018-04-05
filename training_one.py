# -*- coding: utf-8 -*-

import unittest
from abc import ABC, abstractmethod
from collections.abc import Mapping


class Base(ABC):

    @abstractmethod
    def method(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if any('method' in C.__dict__ for C in subclass.__mro__):
            return True
        return NotImplemented('')


class Derived(Base):

    def method(self):
        return 'Implements method abstract'


class MyMapping(Mapping):

    def __init__(self):
        self._value = dict()

    def __iter__(self):
        return iter(self._value.keys())

    def __len__(self):
        return len(self._value.keys())

    def __getitem__(self, key):
        return self._value[key]

    def __setitem__(self, key, value):
        self._value[key] = value


class TestMapping(unittest.TestCase):

    def setUp(self):
        self.mapping = MyMapping()

    def test_len(self):
        self.assertEqual(len(self.mapping), 0)

    def test_insert_key_and_value(self):
        self.mapping['a'] = 'A'
        self.assertEqual(self.mapping['a'], 'A')

'''  
if __name__ == '__main__':
    unittest.main()
'''
