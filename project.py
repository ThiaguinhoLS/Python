# -*- coding: utf-8 -*-


class Model(object):

    def __init__(self):
        self._users = dict()

    @property
    def users(self):
        return self._users



class View(object):

    def __init__(self):
        pass


class Controller(object):

    def __init__(self):
        pass


from threading import Thread

class Th(Thread):

    def __init__(self, number):
        Thread.__init__(self)
        self.number = number

    def run(self):
        print('Initialize Thread')
        print(self.number)


#th = Th(10)
#th.start()


import time

def print_time(nome_thread, delay):
    conta = 0
    while conta < 5:
        time.sleep(delay)
        conta += 1
        print('{0} {1}'.format(nome_thread, time.ctime(time.time())))


thread = Thread(target = print_time('thread', 5))
thread.run()    


