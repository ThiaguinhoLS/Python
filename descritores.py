# -*- coding: utf-8 -*-


class Descriptor(object):

    def __init__(self):
        self._name = ""

    def __get__(self, instance, owner):
        print("Getting : {0}".format(self._name))
        return self._name

    def __set__(self, instance, name):
        print("Setting : {0}".format(name))
        self._name = name.title()

    def __delete__(self, instance):
        print("Deleting : {0}".format(self._name))
        del self._name


class Person(object):

    name = Descriptor()


class Person(object):

    def addProperty(self, attribute):

        getter = lambda self: self._getProperty(attribute)
        setter = lambda self, value: self._setProperty(attribute, value)

        setattr(self.__class__, attribute, property(fget = getter, fset = setter, doc = "Auto gerado"))

    def _getProperty(self, attribute):
        print("Getting {0}".format(attribute))
        return getattr(self, "_" + attribute)

    def _setProperty(self, attribute, value):
        print("Setting {0}".format(attribute))
        setattr(self, "_" + attribute, value)


person = Person()


class Quantidade(object):

    def __init__(self):
        prefixo = self.__class__.__name__
        chave = id(self)
        self.attr = "{0}_{1}".format(prefixo, chave)

    def __get__(self, instance, owner):
        print(self, instance, owner)
        print("Getting {0}".format(self.attr))
        return getattr(instance, self.attr)

    def __set__(self, instance, value):
        print(self, instance, value)


class ItemProduto(object):

    preco = Quantidade()
    peso = Quantidade()

    def __init__(self, nome):
        self._nome = nome




a = ItemProduto("Ervilha")
