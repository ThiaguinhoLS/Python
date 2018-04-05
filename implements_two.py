# -*- coding: utf-8 -*-
# Abstract Factory

import abc
from collections import defaultdict


class Character(object):

    """Random Character"""

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def __repr__(self):
        return "{__class__.__name__}(name = {name})".format(__class__ = self.__class__, name = self._name)

    def interact_with(self, obstacle):
        print("{0} encontrou um {1} e {2}".format(self, obstacle, obstacle.action()))


class Obstacle(object):

    """Random Obstacle"""

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def __repr__(self):
        return "{__class__.__name__}(name = {name})".format(__class__ = self.__class__, name = self._name)

    def action(self):
        return "o derrotou"


class AbstractBuilder(metaclass = abc.ABCMeta):


    """Abstract builder, specific as interface"""

    @abc.abstractmethod
    def make_character(self):
        pass

    @abc.abstractmethod
    def make_obstacle(self):
        pass


class BuilderConcret(AbstractBuilder):

    """Implements AbstractBuilder"""

    def make_character(self):
        return Character("Magician")

    def make_obstacle(self):
        return Obstacle("Ork")


class Singleton(object):

    def __new__(cls, *args):
        if (not hasattr(cls, "_instance")):
            cls._instance = object.__new__(cls)
        return cls._instance


class GameCreator(Singleton):

    def __init__(self, builder):
        self._builder = builder
        self.character = self._builder.make_character()
        self.obstacle = self._builder.make_obstacle()

    def changeBuilder(self, builder):
        self._builder = builder

    def play(self):
        self.character.interact_with(self.obstacle)


def validateAge(name):

    try:
        age = input("{0} Qual sua idade ?: ".format(name))
        age = int(age)
    except ValueError as error:
        print("Idade inválida")
        return (False, age)
    return (True, age)


def main():

    """Main function"""

    name = input("Qual o seu nome ?: ")
    valid_input, age = validateAge(name)
    builder = BuilderConcret()
    game = GameCreator(builder)
    

if __name__ == '__main__':
    main()
