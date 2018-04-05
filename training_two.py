# -*- coding: utf-8 -*-


def return_attrs(instance):

    return [attr for attr in dir(instance) if '__' not in attr]


class Only(object):

    value = 'value'

    def __init__(self):
        self.foo = 'foo'
        self.bar = 'bar'
        self._data = None

    @property
    def data(self):
        return self._data

    
"""

self.__dict__  mostra a namespace somente a nível de instância ('foo', 'bar')
dir(self) mostra o namespace a nível de classe e instância ('foo', 'bar', 'value')

"""


def get_properties_names(obj):
     classname = obj.__class__
     components = dir(classname)
     properties = filter(lambda attr: type(getattr(classname, attr)) is property, components)
     return properties
    

def get_attributes(obj):
    ''' Returns a attributes '''
    namespace = dir(obj)
    all_attributes = list(filter(lambda attr: type(getattr(obj, attr)) is property, namespace))
    return all_attributes


for attr in get_attributes(Only):
    print(attr)











    
