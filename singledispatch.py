# -*- coding: utf-8 -*-

from functools import singledispatch


@singledispatch
def func(arg, verbose = False):
    if (verbose):
        print("Args is : ", end = " ")
    print(arg)


@func.register(str)
def _(arg, verbose = False):
    if (verbose):
        print("Args is string : ", end = " ")
    print(arg)


if (__name__ == "__main__"):
    func(10)
    func(10, verbose = True)
    func("Dog")
    func("Cat", True)
