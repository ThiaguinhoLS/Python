# -*- coding: utf-8 -*-

class Airplane(object):

    def __init__(self):
        self._state = Stopped()

    def __str__(self):
        return 'Airplaine is '

    def set_state(self, state):
        self._state = state

    def on(self):
        self._state.on()

    def off(self):
        self._state.off()


class Movement(object):

    def on(self):
        print('Avião já está ligado')

    def off(self):
        print('Desligando avião')


class Stopped(object):

    def on(self):
        print('Ligando o avião')

    def off(self):
        print('Avião já está desligado')
