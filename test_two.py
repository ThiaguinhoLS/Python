# -*- coding: utf-8 -*-

class Suit(object):

	def __init__(self, name, symbol):
		self._name = name
		self._symbol = symbol

	def __str__(self):
		return self._symbol


class Card(object):

	def __init__(self):
		self._rank = rank
		self._suit = suit

	@property
	def rank(self):
		return self._rank

	@property
	def suit(self):
		return self._suit

	def __str__(self):
		return ':::{0}{1}:::'.format(self._rank, self._suit)