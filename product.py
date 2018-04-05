# -*- coding: utf-8 -*-

import abc
import json
import xml.etree.ElementTree as Etree


class Connector(object):

    @property
    def data(self):
        return self._data


class JSONConnector(Connector):

    """JSON file connector"""

    def __init__(self, filepath):
        self._data = json.loads(filepath)

    @property
    def data(self):
        return self._data


class XMLConnector(Connector):

    """XML file connector"""

    def __init__(self, filepath):
        self._data = Etree.parse(filepath)

    @property
    def data(self):
        return self._data


class Product(object):

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return self._name

    def __repr__(self):
        return "{__class__.__name__}(name = {name}, price = {price})".format(__class__ = self.__class__, name = self._name, price = self._price)


class Delivery(metaclass = abc.ABCMeta):

    def __init__(self, name):
        self._name = self.__class__.__name__

    def __str__(self):
        return self._name


class SEDEX(Delivery):

    value = 5


class PAC(Delivery):

    value = 10
