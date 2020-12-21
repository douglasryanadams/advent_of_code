#!/usr/local/bin/python

def answer_one():
    numbers = set()
    with open('2020_01_input.txt', 'r') as f:
        line = f.readline()
        while line:
            number = int(line)
            if 2020 - number in numbers:
                return (2020 - number) * number
            numbers.add(number)
            line = f.readline()


def answer_two():
    # Brute force;
    numbers = set()
    with open('2020_01_input.txt', 'r') as f:
        line = f.readline()
        while line:
            number = int(line)
            numbers.add(number)
            line = f.readline()
    for alpha in numbers:
        for beta in numbers:
            for gamma in numbers:
                if alpha + beta + gamma == 2020:
                    return alpha * beta * gamma


if __name__ == '__main__':
    # print(answer_one())
    print(answer_two())
