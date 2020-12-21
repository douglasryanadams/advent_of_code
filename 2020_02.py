#!/usr/local/bin/python
import re


def answer_one():
    counter = 0
    pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
    with open('2020_02_input.txt', 'r') as f:
        line = f.readline()
        while line:
            parts = pattern.findall(line)[0]
            lower_bound = int(parts[0])
            upper_bound = int(parts[1])
            char = parts[2]
            password = parts[3]
            print(f'lower_bound: {lower_bound}; upper_bound: {upper_bound}; char: {char}; password: {password}')

            char_count = 0
            for c in password:
                if c == char:
                    char_count += 1
            print(f'char_count: {char_count};')

            if lower_bound <= char_count <= upper_bound:
                print(f'{lower_bound} <= {char_count} <= {upper_bound}')
                counter += 1
            line = f.readline()

    return counter


def answer_two():
    counter = 0
    pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
    with open('2020_02_input.txt', 'r') as f:
        line = f.readline()
        while line:
            parts = pattern.findall(line)[0]
            pos_one = int(parts[0])
            pos_two = int(parts[1])
            char = parts[2]
            password = parts[3]
            if password[pos_one - 1] == char:
                if password[pos_two - 1] != char:
                    counter += 1
            else:
                if password[pos_two - 1] == char:
                    counter += 1
            line = f.readline()
    return counter


if __name__ == '__main__':
    # print(answer_one())
    print(answer_two())
