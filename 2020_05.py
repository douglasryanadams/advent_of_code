#!/usr/local/bin/python
from unittest import TestCase
import sys


def answer_one():
    highest = 0
    with open('2020_05_input.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            seat = find_seat(line)
            if seat > highest:
                highest = seat
            line = f.readline()

    return highest


def answer_two():
    lowest = sys.maxsize
    highest = 0
    seats = set()
    with open('2020_05_input.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            seat = find_seat(line)
            if seat < lowest:
                lowest = seat
            if seat > highest:
                highest = seat
            seats.add(seat)
            line = f.readline()
    seat = lowest
    while seat < highest:
        seat += 1
        if seat not in seats:
            return seat


def find_seat(input_str: str):
    row_lower = 0
    row_upper = 128
    seat_lower = 0
    seat_upper = 8
    print(f'Calculating: {input_str}')

    for c in input_str:
        if c == 'F':
            delta = row_upper - row_lower
            row_upper -= delta / 2
        elif c == 'B':
            delta = row_upper - row_lower
            row_lower += delta / 2
        elif c == 'R':
            delta = seat_upper - seat_lower
            seat_lower += delta / 2
        elif c == 'L':
            delta = seat_upper - seat_lower
            seat_upper -= delta / 2
        print(f'[{row_lower} - {row_upper}] | [{seat_lower} - {seat_upper}]')

    return row_lower * 8 + seat_lower


if __name__ == '__main__':
    # print(answer_one())
    print(answer_two())

test_cases = [
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820)
]


class Test202005(TestCase):

    def test_find_seat(self):
        for input_str, expected in test_cases:
            with self.subTest():
                self.assertEqual(expected, find_seat(input_str))
