# -*- coding: utf-8 -*-


class Singleton(object):

    __instance = None

    @staticmethod
    def create():
        if (not Singleton.__instance):
            Singleton.__instance = object.__new__(Singleton)
        return Singleton.__instance



class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if (not hasattr(cls, "instance")):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class Singleton(object):

    __instance = None

    @staticmethod
    def getInstance():
        if (Singleton.__instance == None):
            Singleton()
        return Singleton.instance

    def __init__(self):
        if (Singleton.__instance != None):
            raise TypeError("This class is a singleton !")
        else:
            Singleton.__instance = self



class Singleton(object):

    def __init__(self, instance):
        self._instance = instance

    def get(self):
        try:
            return self._only
        except AttributeError:
            self._only = self._instance()
            return self._only

    def __call__(self):
        raise TypeError("...")


@Singleton
class Class(object):

    def tell(self):
        return "This is singleton"



def singleton(_class):
    instance = _class()
    def controller():
        return instance
    return controller


@singleton
class Singleton(object):

    def tell(self):
        return "Class as singleton"


a = Singleton()
b = Singleton()
print(id(a), id(b))
