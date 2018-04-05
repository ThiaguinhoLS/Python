# -*- coding: utf-8 -*-

class Publisher(object):

	def __init__(self):
		self.observers = []

	def add(self, observer):
		if observer in self.observers:
			print('Failed in added "{0}"'.format(observer))
		else:
			self.observers.append(observer)

	def remove(self, observer):
		try:
			self.observers.remove(observer)
		except ValueError:
			print('Failed to remover "{0}"'.format(observer))

	def notify(self):
		[observer.notify(self) for observer in self.observers]


class DefaultFormatter(Publisher):

	def __init__(self, name):
		super(DefaultFormatter, self).__init__()
		self.name = name
		self._data = 0

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		try:
			self._data = int(value)
		except ValueError as error:
			print('Error formatted as {0}'.format(value))
		else:
			self.notify()

	def __str__(self):
		return '<{0} : {1} as data = {2}>'.format(type(self).__name__, self.name, self._data)


class HexFormatter(object):

	def notify(self, publisher):

		print('<{0} : {1} has now hexadecimal data = {2}>'.format(
			type(self).__name__, publisher.name, hex(publisher.data))
		)


class BinaryFormatter(object):

	def notify(self, publisher):

		print('<{0} : {1} has now binary data = {2}>'.format(
			type(self).__name__, publisher.name, bin(publisher.data))
		)


def main():

	default = DefaultFormatter('Default Formatted')
	print(default)
	hex_format = HexFormatter()
	bin_format = BinaryFormatter()
	default.add(hex_format)
	default.add(bin_format)
	default.add(hex_format)
	default.data = 16
	default.data = 'Hello'


if __name__ == '__main__':
	main()
