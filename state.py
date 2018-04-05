# -*- coding: utf-8 -*-

from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition

@acts_as_state_machine
class Process(object):

	created = State(initial = True)
	waiting = State()
	running = State()
	terminated = State()
	blocked = State()
	swapped_out_waiting = State()
	swapped_out_blocked = State()

	wait = Event(from_states = (created, running, blocked, swapped_out_waiting), to_state = waiting)
	run = Event(from_states = waiting, to_state = running)
	terminate = Event(from_states = running, to_state = terminated)
	block = Event(from_states = (running, swapped_out_blocked), to_state = blocked)
	swap_wait = Event(from_states = waiting, to_state = swapped_out_waiting)
	swap_block = Event(from_states = blocked, to_state = swapped_out_blocked)

	def __init__(self, name):
		self.name = name

	@after('wait')
	def wait_info(self):
		print('{0} entered waiting mode'.format(self.name))

	@after('run')
	def run_info(self):
		print('{0} is running'.format(self.name))

	@before('terminate')
	def terminate_info(self):
		print('{0} terminated'.format(self.name))

	@after('block')
	def block_info(self):
		print('{0} is blocked'.format(self.name))

	@after('swap_wait')
	def swap_wait_info(self):
		print('{0} is swapped out and waiting'.format(self.name))

	@after('swap_block')
	def swap_block_info(self):
		print('{0} is swapped out and blocked'.format(self.name))


def transition(process, event, event_name):

	try:
		event()
	except InvalidStateTransition as error:
		print('Error : transition of {0} from {1} to {2} failed'.format(process.name, process.current_state, event_name))


def state_info(process):

	print('State of {0} : {1}'.format(process.name, process.current_state))


def main():

	RUNNING = 'running'
	WAITING = 'waiting'
	BLOCKED = 'blocked'
	TERMINATED = 'terminated'
	p_one, p_two = Process('Process_one'), Process('Process_two')
	[state_info(process) for process in (p_one, p_two)]
	print('')
	transition(p_one, p_one.wait, WAITING)
	transition(p_two, p_two.terminate, TERMINATED)
	[state_info(process) for process in (p_one, p_two)]
	print('')
	transition(p_one, p_one.run, RUNNING)
	transition(p_two, p_two.wait, WAITING)
	[state_info(process) for process in (p_one, p_two)]
	print('')
	transition(p_two, p_two.wait, RUNNING)
	[state_info(process) for process in (p_one, p_two)]
	print('')
	[transition(process, process.block, BLOCKED) for process in (p_one, p_two)]
	[state_info(process) for process in (p_one, p_two)]
	print('')
	[transition(process, process.terminate, TERMINATED) for process in (p_one, p_two)]
	[state_info(process) for process in (p_one, p_two)]


if __name__ == '__main__':
	main()
