# -*- coding: utf-8 -*-

class Handle(object):

    def state(self):
        raise NotImplementedError


class HandleConcretA(Handle):

    def state(self):
        print('State A')


class HandleConcretB(Handle):

    def state(self):
        print('State B')


class Only(object):

    def __init__(self):
        self._implementation = HandleConcretA()

    def state(self):
        return self._implementation.state()


def main():

    only = Only()
    only.state()
    only._implementation = HandleConcretB()
    only.state()


if __name__ == '__main__':
    main()
