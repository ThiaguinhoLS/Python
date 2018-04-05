# -*- coding: utf-8 -*-

import time

def pairs(seq):

	n = len(seq)

	for i in range(n):

		yield seq[i], seq[i + 1 % n]

SLOW = 3

LIMIT = 5

WARNING = 'too bad, you picked teh slow algorithm :('

def allUniqueSort(s):

	if len(s) > LIMIT:

		print(WARNING)

		time.sleep(SLOW)

	srtStr = sorted(s)

	for c_one, c_two in pairs(srtStr):

		if c_one == c_two:

			return False

	return True


def allUniqueSet(s):

	if len(s) > LIMIT:

		print(WARNING)

		time.sleep(SLOW)

	return True if len(set(s)) == len(s) else False


def allUnique(s, strategy):

	return strategy(s)


def main():

    while True:

        word = None

        while not word:

            word = input('Insert word (type quit to exit)> ')

            if word == 'quit':

                print('bye')

                return

            strategy_picked = None

            strategies = { '1': allUniqueSet, '2': allUniqueSort }

            while strategy_picked not in strategies.keys():

                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')

                try:

                    strategy = strategies[strategy_picked]

                    print('allUnique({0}): {1}'.format(word, allUnique(word, strategy)))

                except KeyError as err:

                    print('Incorrect option: {0}'.format(strategy_picked))

            print()


if __name__ == '__main__':
	main()

