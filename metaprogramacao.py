# -*- coding: utf-8 -*-

from collections import OrderedDict

class Meta(type):

    @classmethod
    def __prepare__(metaclass, name, bases):
        print("__prepare__")
        print(metaclass, name, bases)
        return OrderedDict()

    def __new__(cls, name, bases, namespace):
        print("__new__")
        print(cls, name, bases, namespace)
        result = type.__new__(cls, name, bases, namespace)
        return result


class Class(object, metaclass = Meta):


    def a(self): pass
    def b(self): pass
    def c(self): pass

    def view_attributes(self):
        return [attr for attr, value in self.__dict__ if (not attr.startswith("__"))]



print(Class().view_attributes())

