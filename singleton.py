# -*- coding: utf-8 -*-


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if (not hasattr(cls, "instance")):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.value = "Singleton"

    def __str__(self):
        return repr(self) + self.value



class Borg(object):

    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state


class OnlyOne(Borg):

    def __init__(self, val):
        super(OnlyOne, self).__init__()
        self.val = val

    def __str__(self):
        return "{0}{1}".format(id(self.__dict__), self.val)


class GenericSingleton(object):

    def __new__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        if (not hasattr(cls, "instance")):
            cls.instance = super(GenericSingleton, cls).__new__(cls)
        return cls.instance


class Ponto(GenericSingleton):

    def __init__(self, value):
        self.value = value


class UniqueClass(object):

    __instance = None

    def __init__(self):
        if (UniqueClass.__instance != None):
            raise Exception("Class is Singleton")
        UniqueClass.__instance = self

    @staticmethod
    def getInstance():
        if (UniqueClass.__instance == None):
            UniqueClass()
        return UniqueClass.__instance


class OnlyClass(object):

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


@OnlyClass
class Class(object):

    def tell(self):
        return "Class is Singleton"
