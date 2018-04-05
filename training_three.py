# -*- coding: utf-8 -*-

class No(object):

	def __init__(self, carga = None, proximo = None):
		self.carga = carga
		self.proximo = proximo

	def __str__(self):
		return str(self.carga)


def imprimeLista(no):

	while no:
		print(no)
		no = no.proximo
	print('')



no1 = No(1)
no2 = No(2)
no3 = No(3)

no1.proximo = no2
no2.proximo = no3

imprimeLista(no1)