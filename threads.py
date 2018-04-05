# -*- coding: utf-8 -*-


from threading import Thread
from time import sleep

lista = []

def count(x):
    global lista
    for i in range(x):
        lista.append(i)
    print('Finish\n')


t = Thread(target = lambda: count(300))

t.start()

while t.is_alive():
    print('Thread is alive')
