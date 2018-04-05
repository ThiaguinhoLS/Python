# -*- codimg: utf-8 -*-


class OnlyClass(object):

	def __init__(self, value):

		self.value = value

	def __str__(self):

		return self.value


class Only(object):

	@classmethod
	def products(cls):

		return 'OnlyClass'


product = Only.products()

this_module = __import__(__name__)
print(dir(this_module))
classe = getattr(this_module, product)
print(classe)
