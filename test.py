class Singleton:
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
class Class:
  def tell(self):
    print("This is singleton.")



class Decorator(object):

    def __init__(self, singleton):
        self._singleton = singleton

    def __call__(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._singleton()
            return self._instance


@Decorator
class Single(object):

    def tell(self):
        return "Class is Singleton"


class Singleton(object):

    def __new__(cls):
        if (not hasattr(cls, "_instance")):
            cls._instance = object.__new__(cls)
        return cls._instance

class OnlySingleton(Singleton):

    def tell(self):
        return "Class is Singleton"



class Singleton(object):

    _instance = None

    def __init__(self):
        if (Singleton._instance != None):
            raise Exception("Class is Singleton")
        Singleton._instance = self

    def get(self):
        if (Singleton._instance == None):
            Singleton()
        return Singleton._instance


# Factory method


import abc


class Shape(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def draw(self):
        pass


class Triangle(Shape):

    def draw(self):
        return "I am a triangular shape"


class Square(Shape):

    def draw(self):
        return "I am a square shape"


def createShapes(sides):

    if (sides == 3):
        return Triangle()
    elif (sides == 4):
        return Square()
    else:
        raise Exception("Error")


from enum import Enum
from random import randint


Card = Enum('Card', 'Club Diamond Heart Spades')


class Cards(object):

    _shared = {}

    def __new__(cls, rank, suit):
        obj = cls._shared.get(suit, None)
        if obj is None:
            obj = object.__new__(cls)
            cls._shared[suit] = obj
            obj.rank, obj.suit = rank, suit
        return obj

    def __str__(self):
        return '{0} {1}'.format(self.rank, self.suit)



def main():

    """Main function"""

    card_one = Cards("A", Card.Club)
    card_two = Cards("2", Card.Club)

    print(id(card_one), id(card_two))
    print(card_one)
    print(card_two)


if __name__ == '__main__':
    main()
