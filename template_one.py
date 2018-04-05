# -*- coding: utf-8 -*-

from time import sleep

SLEEP_TIME = 3

class Pizza(object):

    def __init__(self):
        self.type_name = self.__class__.__name__

    def add_ingredients(self):
        for ingredient in self._ingredients:
            print('Adding {0}'.format(ingredient))
            sleep(self._time)
        print('Pizza of {0} finished !'.format(self))

    def __str__(self):
        return self.type_name


class Margarita(Pizza):

    _ingredients = ['cheese', 'bacon', 'calabresa']
    _time = 3


def main():

    mortadela = Margarita()

    mortadela.add_ingredients()


if __name__ == '__main__':
    main()
