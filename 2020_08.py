#!/usr/local/bin/python
from unittest import TestCase


def answer_one():
    with open('2020_07_input.txt', 'r') as f:

        line = f.readline()
        while line:
            line = f.readline()


def answer_two():
    with open('2020_07_input.txt', 'r') as f:
        line = f.readline()
        while line:
            line = f.readline()
    pass


if __name__ == '__main__':
    print(answer_one())
    # print(answer_two())
