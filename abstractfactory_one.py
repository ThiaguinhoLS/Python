# -*- coding: utf-8 -*-

class Mago(object):

    def __init__(self, nome):
        self.nome = nome

    def method(self, vilao):
        print('{0} encontrou um {1} e {2} !'.format(self, vilao, vilao.acao()))

    def __str__(self):
        return self.nome


class Ogro(object):

    def __str__(self):
        return 'Ogro'

    def acao(self):
        return 'o derrotou'


class Sapo(object):

    def __init__(self, nome):
        self.nome = nome

    def method(self, vilao):
        print('{0} encontrou uma {1} e {2} !'.format(self, vilao, vilao.acao()))

    def __str__(self):
        return self.nome


class Folha(object):

    def __str__(self):
        return 'Folha'

    def acao(self):
        return 'a comeu'


class MundoMago(object):

    def __init__(self, nome):
        self.nome = nome

    def criar_heroi(self):
        return Mago(self.nome)

    def criar_vilao(self):
        return Ogro()


class MundoSapo(object):

    def __init__(self, nome):
        self.nome = nome

    def criar_heroi(self):
        return Sapo(self.nome)

    def criar_vilao(self):
        return Folha()
    

class Game(object):

    def __init__(self, fabrica):
        self.heroi = fabrica.criar_heroi()
        self.vilao = fabrica.criar_vilao()

    def play(self):
        self.heroi.method(self.vilao)


def valida_idade():
    valida = False
    while not valida:
        idade = input('Digite sua idade : ')
        try:
            idade = int(idade)
            if idade > 0 and idade < 65:
                valida = True
        except ValueError as error:
            print('Idade não é válida !')
    return idade


def main():
    while True:
        nome = input('Qual o seu nome ?: ')
        print('Seja bem-vindo {0}'.format(nome))
        idade = valida_idade()
        game = MundoSapo if idade < 18 else MundoMago
        principal = Game(game(nome))
        principal.play()


if __name__ == '__main__':
    main()



