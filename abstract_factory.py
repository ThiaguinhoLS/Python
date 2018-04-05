# -*- coding: utf-8 -*-

import random
import inspect
from abc import ABC, abstractmethod


class Polygon(ABC):

    def __init__(self, factory_name = None):
        self._color = 'black'
        self._manufactured = factory_name

    def __str__(self):
        return '{0} {1} manufactured by {2} (perimeter : {3}, area : {4}'.format(self.color, self.__class__.__name__, self._manufactured, \
                                                                                 self.perimeter, self.area)

    @property
    @abstractmethod
    def family(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def manufactured(self):
        return self._manufactured

    @manufactured.setter
    def manufactured(self, factory_name):
        self._manufactured = factory_name


class Triangle(Polygon):

    @property
    def family(self):
        return 'Triangles'

    @property
    def perimeter(self):
        return 'A + B + C'

    @property
    def area(self):
        return 'BASE * HEIGHT / 2'


class TriangleEquilateral(Triangle):

    @property
    def perimeter(self):
        return '3A'


class TriangleIsosceles(Triangle):

    @property
    def perimeter(self):
        return '2A + B'


class TriangleScalene(Triangle):

    pass


class Quadrilateral(Polygon):

    @property
    def family(self):
        return 'Quadrilaterals'

    @property
    def perimeter(self):
        return 'A + B + C + D'

    @property
    def area(self):
        return 'Bretschneider"s formula'


class Square(Quadrilateral):

    @property
    def perimeter(self):
        return '4A'

    @property
    def area(self):
        return 'A * A'


class Rectangle(Quadrilateral):

    @property
    def perimeter(self):
        return '2A + 2B'

    @property
    def area(self):
        return 'BASE * HEIGHT'


class ConvexQuadrilateral(Quadrilateral):

    pass


def give_me_some_polygons(factories, color = None):
    """
    factories : list
    color: str
    
    """
    if not isinstance(factories, list):
        factories = [factories]

    products = list()
    for factory in factories:
        num = random.randint(5, 10)
        for i in range(num):
            product = factory.make_polygon(color)
            products.append(product)

    return products

    
def main():
    triangles = give_me_some_polygons(TriangleFactory)
    print('{0} triangles'.format(len(triangles)))
    for triangle in triangles:
        print_polygon(triangle)


class PolygonFactory(ABC):

    @classmethod
    @abstractmethod
    def products(cls):
        pass

    @classmethod
    @abstractmethod
    def make_polygon(cls, color = None):
        """

            color: str
            
        """

        product_name = random.choice(cls.products())
        this_module = __import__(__name__)
        polygon_class = getattr(this_module, product_name)
        polygon = polygon_class(factory_name = cls.__name__)
        if color is not None:
            polygon.color = color
        return polygon

    @classmethod
    @abstractmethod
    def color(cls):
        return 'black'


class TriangleFactory(PolygonFactory):

    @classmethod
    @abstractmethod
    def products(cls):
        return tuple(['TriangleEquilateral', 'TriangleIsosceles', 'TriangleScalene'])


class QuadrilateralFactory(PolygonFactory):

    @classmethod
    @abstractmethod
    def products(cls):
        return tuple(['Square', 'Rectangle', 'ConvexQuadrilateral'])


def print_polygon(polygon, show_repr = False, show_hierarchy = False):
    print(str(polygon))
    if show_repr:
        print(repr(polygon))
    if show_hierarchy:
        print(inspect.getmro(polygon.__class__))
        print('\n')


if __name__ == '__main__':
    main()
