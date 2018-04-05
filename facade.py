# -*- coding: utf-8 -*-

from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')


class Server(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart = True):
        pass


class FileServer(Server):

    def __init__(self):
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print('Booting the {0}'.format(self))
        self.state = State.running

    def kill(self, restart = True):
        print('Killing {0}'.format(self))
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        print('Trying to create the file "{0}" for user "{1}" with permissions "{2}"'.format(name, user, permissions))


class ProcessServer(Server):

    def __init__(self):
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print('Booting the {0}'.format(self))
        self.state = State.running

    def kill(self, restart = True):
        print('Killing {0}'.format(self))
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        print('Trying to create the process "{0}" for user "{1}"'.format(name, user))



class System(object):

    def __init__(self):
        self.file_server = FileServer()
        self.process_server = ProcessServer()

    def start(self):
        [server.boot() for server in (self.file_server, self.process_server)]

    def create_file(self, user, name, permissions):
        return self.file_server.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.process_server.create_process(user, name)


def main():
    os = System()
    os.start()
    os.create_file('Thiago', 'archive.txt', '-rw-r-r')
    os.create_process('bar', 'ls/tmp')


if __name__ == '__main__':
    main()
