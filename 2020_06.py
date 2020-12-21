#!/usr/local/bin/python
from unittest import TestCase


def answer_one():
    total = 0

    with open('2020_06_input.txt', 'r') as f:
        yes_set = set()

        line = f.readline()
        while line:
            line = line.rstrip()
            if line:
                for c in line:
                    yes_set.add(c)
            else:
                total += len(yes_set)
                yes_set = set()
            line = f.readline()

        total += len(yes_set)

    return total


def answer_two():
    total = 0

    with open('2020_06_input.txt', 'r') as f:
        yes_dict = dict()
        line_count = 0

        line = f.readline()
        while line:
            line = line.rstrip()
            if line:
                print(line)
                line_count += 1
                for c in line:
                    c_count = yes_dict.get(c, 0)
                    yes_dict[c] = c_count + 1

            else:
                print('Adding: ', end='')
                for letter, letter_count in yes_dict.items():
                    if letter_count == line_count:
                        print(letter, end='')
                        total += 1
                yes_dict = dict()
                line_count = 0
                print('')
                print('-----------')

            line = f.readline()

    print('Adding: ', end='')
    for letter, letter_count in yes_dict.items():
        if letter_count == line_count:
            print(letter, end='')
            total += 1
    print('')

    return total


if __name__ == '__main__':
    # print(answer_one())
    print(answer_two())
