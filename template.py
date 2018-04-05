# -*- coding: utf-8 -*-
from string import Template

class MyTemplate(Template):

	"""Implementando heranão de Template alterando assim seu delimitador"""

	delimiter = '#'


def main():

	fruits = {
		'apple': 1.058,
		'pineapple': 0.55
	}

	t = MyTemplate('The #name costs R$ #value.')

	for fruit, value in fruits.items():
		print(t.substitute(name = fruit, value = value))

if __name__ == '__main__':
	main()
