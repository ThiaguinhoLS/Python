# -*- coding: utf-8 -*-

from itertools import product


class Send(object):

    def __init__(self, name, rate):
        self._name = name
        self._rate = rate

    def __str__(self):
        return self._name

    def send_value(self, product):
        return product.price * self._rate



class Product(object):

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price is not valid !')
        self._price = value


def main():

    cheese = Product('Cheese', 10)
    chocolat = Product('Chocolate', 5)
    sedex = Send(name = 'Sedex', rate = .1)
    pac = Send(name = 'Pac', rate = .05)

    for prod, method in product((cheese, chocolat), (sedex, pac)) :
        print('Product : {0}, Price : R$ {1}'.format(prod, prod.price))
        print('Mode of Send : {0}'.format(method))
        print('Price : R$ {0}'.format(method.send_value(prod)))


if __name__ == '__main__':
    main()
