# -*- coding: utf-8 -*-
'''
def foo(x):
    try:
        1 / 0
    except ZeroDivisionError as error:
        print('Error ZeroDivisionError')
        print(dir(error))
        print('context', error.__context__)
        print('supress_context_', error.__suppress_context__)
        print('cause', error.__cause__)
        raise Exception('New Error') from error


def bar(x):
    try:
        foo('init')
    except Exception as error:
        print('context', type(error.__context__))
        print('supress_context_', error.__suppress_context__)

bar('init')
'''
'''
Quando levantada uma exceção numa claúsula 'except' seu '__context__' é definido como a exceção ao qual ela pertence no tratamento da
exemplo :
    try:
        1 / 0
    except ZeroDivisionError:
        raise Exception from None
O contexto da segunda exceção é a primeira exceção ao qual ele faz parte

'''

class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

for cls in [A, B, C]:
    try:
        raise cls()
    except C:
        print('C')
    except B:
        print('B')
    except A:
        print('A')

'''
while True:
    entry = input('Enter as value : ')
    try:
        entry = int(entry)
    except ValueError:
        print('Value is not valid')
    except KeyboardInterrupt:
        print('Bye')
    else:
        print('Value is ', value)
'''








import sys

try:
    #f = open('myfile.txt', mode = 'r')
    s = f.readline()
    i = int(s.strip())
except OSError as err: # Classe usada como base para FileNotFoundError capturará de forma correta a exceção
    print('OSError as {0}'.format(err))
except ValueError:
    print('ValueError')
except:
    print('Unexpected error', sys.exc_info()[0]) # Retorna a última exceção levantada
    raise
