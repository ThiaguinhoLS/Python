# -*- coding: utf-8 -*-

import os


def deleteFile(filepath, verbose = True):
    if verbose:
        print('Deleting {0}'.format(filepath))
    os.remove(filepath)


class RenameFile(object):

	def __init__(self, path_src, path_dest):
		self.src = path_src
		self.dest = path_dest

	def execute(self, verbose = True):
		if verbose:
			print('[Renaming "{0}" to "{1}"]'.format(self.src, self.dest))
		os.rename(self.src, self.dest)

	def undo(self, verbose = True):
		if verbose:
			print('[Renaming "{0}" back to "{1}"]'.format(self.dest, self.src))
		os.rename(self.dest, self.src)


class CreateFile(object):

	def __init__(self, path, text = 'Hello World\n'):
		self.path = path
		self.text = text

	def execute(self, verbose = True):
		if verbose:
			print('Creating file "{0}"'.format(self.path))
		with open(self.path, mode = 'w', encoding = 'utf-8') as archive:
			archive.write(self.text)

	def undo(self):
		deleteFile(self.path)


class ReadFile(object):

	def __init__(self, filepath):
		self.filepath = filepath

	def execute(self, verbose = True):
		if verbose:
			print('Reading "{0}"'.format(self.filepath))
		with open(self.filepath, mode = 'r') as archive:
			print(archive.read())


def main():

    orig_file, new_file = 'file_one.txt', 'file_two.txt'
    commands = []
    for obj in (CreateFile(orig_file), ReadFile(orig_file), RenameFile(orig_file, new_file)):
        commands.append(obj)
        [command.execute() for command in commands]
        option = input('Reverse the execute commands [y/n] ?: ')
        if option not in 'Yy':
	print('Results is : "{0}"'.format(new_file))
	raise SystemExit
        for command in commands:
	try:
                command.execute()
                print('Reversed ...')
	except AttributeError:
	    pass


if __name__ == '__main__':
	main()

