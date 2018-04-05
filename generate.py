# -*- coding: utf-8 -*-


from random import randint


def formated_list(list_of_numbers):
    for i in range(0, 20, 5):
        j = i + 5
        yield list_of_numbers[i:j]



def generate_numbers(number):

    assert number > 0

    print('Creating ...\n')

    for _ in range(number):
        numbers = []
        while len(numbers) < 20:
            number = randint(0, 100)
            if number in numbers:
                continue
            numbers.append(number)
        yield numbers

    print('Created list of numbers')


def main():

    valid_input = False
    while not valid_input:
        number = input('Enter as number : ')
        try:
            number = int(number)
        except ValueError as error:
            print('Number is not valid')
        else:
            valid_input = True

    print('List of numbers randoms')

    for numbers in generate_numbers(number):
        for i in formated_list(numbers):
            print('{0}'.format(' '.join(map(str, i))))
        print('\n')


if __name__ == '__main__':
    main()
