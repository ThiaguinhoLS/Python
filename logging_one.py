# -*- coding: utf-8 -*-

import logging

# logging.disable(level = logging.CRITICAL) Desativa os a execução do logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s') # Configuração

logging.debug('Start of program')

def factorial(n):
    logging.debug(f'Start a factorial of {n}')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug(f'End a factorial {n}')
    return total


print(factorial(5))
logging.debug('End of program')
    
