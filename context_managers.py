# -*- coding: utf-8 -*-

import contextlib

import os

@contextlib.contextmanager
def _chdir(directory):
	orig = os.getcwd()
	os.chdir(directory)
	try:
		yield
	finally:
		os.chdir(orig)


class ManagedFile(object):

	def __init__(self, name):
		self.name = name

	def __enter__(self):
		self.file = open(self.name, mode = 'w')
		return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.file:
			self.file.close()


@contextlib.contextmanager
def enter_file(name, mode = 'r'):

	try:
		f = open(name, mode)
		yield f
	except FileNotFoundError:
		f = open(name, 'w')
		f.write('')
		yield f
	finally:
		f.close()


with ManagedFile('hello.txt') as f:
	f.write('Hello World\n')

print('')

with enter_file('notexists.txt') as f:
	print(f.read())


def generate_things():
	print('first thing')
	yield
	print('second thing')


value = 0

lists = [1, 2, 3, [4, 5, 6], 7, [8, 9]]


def iter_list(iterable):

	global value # Usando uma variável global

	for i in iterable:
		if isinstance(i, list):
			iter_list(i)
		else:
			value += i

iter_list(lists)

print(value)