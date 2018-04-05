# -*- coding: utf-8 -*-

class Event(object):

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name


class Widget(object):

	def __init__(self, parent = None):
		self.parent = parent

	def handle(self, event):
		handler = 'handle_{0}'.format(event)

		if hasattr(self, handler):
			method = getattr(self, handler)
			method(event)
		elif self.parent:
			self.parent.handle(event)
		elif hasattr(self, 'handle_default'):
			self.handle_default(event)


class MainWindow(Widget):

	def handle_close(self, event):
		print('MainWindow : {0}'.format(event))

	def handle_default(self, event):
		print('MainWindow Default: {0}'.format(event))


class SendDialog(Widget):

	def handle_paint(self, event):
		print('SendDialog : {0}'.format(event))


class MSGText(Widget):

	def handle_down(self, event):
		print('MSGText : {0}'.format(event))


def main():

	mw = MainWindow()
	sd = SendDialog(mw)
	msg = MSGText(sd)
	for e in ('down', 'paint', 'unhandled', 'close'):
		event = Event(e)
		print('Sending event -{0}- to MainWindow'.format(event))
		mw.handle(event)
		print('Sending event -{0}- to SendDialog'.format(event))
		sd.handle(event)
		print('Sending event -{0}- to MSGText'.format(event))
		msg.handle(event)


if __name__ == '__main__':
	main()




