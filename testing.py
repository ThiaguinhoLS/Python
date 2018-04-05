# -*- coding: utf-8 -*- 

class State(object):

	def handler(self):
		raise NotImplementedError
		

class ConcretStateA(State):
	
	def handler(self):
		return 'Implements ConcretStateA'
		

class ConcretStateB(State):

	def handler(self):
		return 'Implements ConcretStateB'
		


class Context(object):

	def __init__(self):
		self._state = ConcretStateA()
		
	def set_state(self, state):
		self._state = state
		
	def handler(self):
		print(self._state.handler())
		


class ContextManager(object):

	def __init__(self, filepath):
		self.filepath = filepath

	def __enter__(self):
		return open(self, mode = 'w', encoding = )

if __name__ == '__main__':
	
	context = Context()
	state_b = ConcretStateB()
	context.handler()
	context.set_state(state_b)
	context.handler()
		
	

