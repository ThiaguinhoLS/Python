# -*- coding: utf-8 -*-

class Decorator(object):

    def __init__(self, method):
        self.method = method

    def __call__(self, *args, **kwargs):
        return self.method(*args, **kwargs)


@Decorator
def soma(x, y):
    return x + y


if __name__ == '__main__':
    value = soma(1, 4)
    print(value)
