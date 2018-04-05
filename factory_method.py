# -*- coding: utf-8 -*-


class Car(object):

    pass


class Bike(object):

    pass



def factory_method(product_type):

    if product_type == 'car':
        return Car()
    elif product_type == 'bike':
        return Bike()
    else:
        raise ValueError('Cannot make : {0}'.format(product_type))


def main():
    for product_type in ('car', 'bike'):
        product = factory_method(product_type)
        print(str(product))


if __name__ == '__main__':
    main()
