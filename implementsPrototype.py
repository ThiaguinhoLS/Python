# -*- coding: utf-8 -*-



def _copy(obj, original):
    obj,__dict__.update(original.__dict__)


class Only(object):

    pass


class Prototype(object):

    def copy(self):
        return copy.copy(self)

    def deepcopy(self):
        return copy.deepcopy(self)
