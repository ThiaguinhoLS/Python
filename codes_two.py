# -*- coding: utf-8 -*-

import logging

# Configuração do log
logging.basicConfig(
    filename = 'calculadora.log',
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(funcName)s => %(message)s'
)

def add(x, y):
    logging.debug(f'parameters: x = {x}, y = {y}')
    return x + y

def sub(x, y):
    logging.debug(f'parameters: x = {x}, y = {y}')
    return x - y

def mul(x, y):
    logging.debug(f'parameters: x = {x}, y = {y}')
    return x * y

def div(x, y):
    logging.debug(f'parameters: x = {x}, y = {y}')
    try:
        return x / y
    except ZeroDivisionError as err:
        logging.exception(f'parameters = {x}, y = {y}')
        print('Impossível dividir por 0')


if __name__ == '__main__':
    print(add(8, 4))
    print(sub(2, 1))
    print(div(1, 0))
    print(div(2, 1))
    print(mul(2, 5))
