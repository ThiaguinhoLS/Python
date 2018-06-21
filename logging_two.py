# -*- coding: utf-8 -*-

import logging
from datetime import datetime

# Configuração de arquivo de log onde:
# filename: Nome do arquivo
# filemode: Paramêtros do arquivo w: cria um novo arquivo
# level: Nível padrão das captura das mensagens, podendo ser tanto um int entre [10, 20 ... 50] ou um [logging.DEBUG, logging.INFO ...]
# format: Formato da mensagem
# datefmt = Formato da data e hora

logging.basicConfig(
    filename = 'example.log',
    filemode = 'w',
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s: %(message)s',
    datefmt = '%d/%m/%Y %I:%M:%S %p'
)

logging.debug('Program in debug to log file in {}'.format(datetime.now()))
logging.info('So should this')
logging.warning('And this, too')

with open('example.log') as f:
    print(f.read().strip())
