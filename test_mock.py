# -*- coding: utf-8 -*-

import mock

# Dummy

class Carro(object):

    rodas = 4

    def __init__(self, descricao, fabricante):
        self.descricao = descricao
        self.fabricante = fabricante


def test_usando_dummy():

    fabricante = None
    carro = Carro('Fusca', fabricante)

    assert carro.rodas == 4


test_usando_dummy()


# Fake


class Carro(object):

    rodas = 4

    def __init__(self, descricao, fabricante):
        self.descricao = descricao
        self.fabricante = fabricante

    def __str__(self):
        return '{0} ({1})'.format(self.descricao, self.fabricante.get_descricao())


class FabricanteFake(object):

    descricao = 'Volkswagen'

    def get_descricao(self):
        return self.descricao


def test_usando_fake():

    fabricante = FabricanteFake()
    carro = Carro('Fusca', fabricante)

    assert str(carro) == 'Fusca (Volkswagen)'


test_usando_fake()



class Carro(object):

    rodas = 4

    def __init__(self, descricao, fabricante):
        self.descricao = descricao
        self.fabricante = fabricante

    def __str__(self):
        return '{0} ({1})'.format(self.descricao, self.fabricante.get_descricao())


def test_usando_mock():

    fabricante = mock.MagicMock()
    fabricante.get_descricao.return_value = 'Volkswagen'
    carro = Carro('Fusca', fabricante)

    assert str(carro) == 'Fusca (Volkswagen)'

    fabricante.get_descricao.assert_called_once_with()


test_usando_mock()

