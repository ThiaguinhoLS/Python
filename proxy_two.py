# -*- coding: utf-8 -*-

from abc import ABCMeta
import sys


class Wrapper(object):

    _instance = None

    class SensitiveInfo(object):

        def __init__(self):
            self.users = ['mick', 'tom', 'ben', 'mike']

        def read(self):
            print('There are {0} users : {1}'.format(len(self.users), ' '.join(self.users)))

        def add(self, user):
            self.users.append(user)
            print('Added user {0}'.format(user))

        def remove(self, user):
            self.users.remove(user)
            print('Removed user {0}'.format(user))


    def __init__(self):
        if not hasattr(self.__class__, '_instance'):
            self.__class__._instance = self.SensitiveInfo()



class Info(object):

    def __init__(self):
        self.protected = Wrapper()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('What is the secret ?: ')
        self.protected.add(user) if self.secret == sec else print('That"s wrong !')

    def remove(self, user):
        sec = input('What is the secret ?: ')
        if self.secret == sec and user in self.protected.users:
            self.protected.remove(user)
        else:
            print('That"s wrong !')


def main():

    info = Info()

    while True:
        print('[1] - Read\n[2] - Add user\n[3] - Remove user\n[4] - Quit')
        key = input('Choose option ?: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('Choose a username ?: ')
            info.add(name)
        elif key == '3':
            name = input('Choose a username ?: ')
            info.remove(name)
        elif key == '4':
            sys.exit()
        else:
            print('Option is not valid')


if __name__ == '__main__':
    main()
