# -*- coding: utf-8 -*-

from abc import ABCMeta
import xml.etree.ElementTree as ET
import json


def connect_to(filepath):
    if filepath.endswith('.json'):
        connect = JSONConnector
    elif filepath.endswith('.xml'):
        connect =  XMLConnector
    else:
        raise Exception('Connection is not valid')
    return connect(filepath)


class Connector(metaclass = ABCMeta):

    def __init__(self, filepath):
        self._filepath = filepath

    @property
    def data(self):
        return self.data


class JSONConnector(Connector):

    def __init__(self, filepath):
        self._data = dict()


class XMLConnector(Connector):

    def __init__(self):
        pass



class Model(object):

    def __init__(self, filepath):
        self._filepath = filepath


class View(object):

    def show(self):
        pass

    def error(self, error):
        print(error)


class Controller(object):

    pass
