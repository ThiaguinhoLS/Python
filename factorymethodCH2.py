# -*- coding: utf-8 -*-

import abc

class Shape(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def draw(self):
        pass


class Square(Shape):

    def __init__(self):
        self._name = "Square"

    def draw(self):
        return "The shape is a {0}".format(self._name)


class Triangle(Shape):

    def __init__(self):
        self._name = "Triangle"

    def draw(self):
        return "The shape is a {0}".format(self._name)


def factoryShape(number_of_sides):

    """Factory to create Shapes"""

    if (number_of_sides == 3):
        return Triangle()
    elif (number_of_sides == 4):
        return Square()
    else:
        raise Exception("Shape is inválid")


def main():
    """Function main"""

    triangle = factoryShape(3)
    print(triangle.draw())
    square = factoryShape(4)
    print(square.draw())


if (__name__ == "__main__"):
    main()
