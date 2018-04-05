# -*- coding: utf-8 -*-


class Singleton(object):

    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception('Class is a Singleton')
        Singleton._instance = self


class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance


class Singleton(object):

    def __init__(self, instance):
        self._instance = instance

    def __call__(self, *args, **kwargs):
        try:
            return self._only
        except AttributeError:
            self._only = self._instance(*args, **kwargs)
            return self._only


@Singleton
class Only(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Borg(object):

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class BorgOne(Borg):

    def __init__(self):
        self.x = 'X'


class BorgTwo(Borg):

    def __init__(self):
        self.y = 'Y'


class Computer(object):

    class MacComputer(object):

        def __init__(self, memory, number_series):
            self._memory = memory
            self._number_series = number_series

        def __str__(self):
            info = (
                'Number series : {0}'.format(self._number_series),
                'Memory : {0}'.format(self._memory)
            )
            return '\n'.join(info)

    def get_computer(self, memory, number_series):
        return self.MacComputer(memory, number_series)


computer = Computer()
mac_computer = computer.get_computer("4Gb", "AX154D")
print(mac_computer)
