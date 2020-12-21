#!/usr/local/bin/python

def answer_one():
    tree_matrix = []
    with open('2020_03_input.txt', 'r') as f:
        line = f.readline()
        while line:
            row = []
            for pos in line:
                if pos == '.':
                    row.append(False)
                elif pos == '#':
                    row.append(True)
            tree_matrix.append(row)
            line = f.readline()

    return find_trees(tree_matrix, 1, 3)


def answer_two():
    tree_matrix = []
    with open('2020_03_input.txt', 'r') as f:
        line = f.readline()
        while line:
            row = []
            for pos in line:
                if pos == '.':
                    row.append(False)
                elif pos == '#':
                    row.append(True)
            tree_matrix.append(row)
            line = f.readline()
    alpha = find_trees(tree_matrix, 1, 1)
    beta = find_trees(tree_matrix, 3, 1)
    gamma = find_trees(tree_matrix, 5, 1)
    delta = find_trees(tree_matrix, 7, 1)
    epsilon = find_trees(tree_matrix, 1, 2)
    return alpha * beta * gamma * delta * epsilon


def find_trees(tree_matrix, right: int, down: int):
    height = len(tree_matrix)
    width = len(tree_matrix[0])
    print(f'height: {height}; width: {width}')

    row = 0
    column = 0
    counter = 0
    while row < (height - down):
        row += down
        column += right
        column_index = column % width
        print(f'({row},{column})|tree_matrix[{row}][{column_index}]: {tree_matrix[row][column_index]}')
        if tree_matrix[row][column_index]:
            counter += 1
    return counter


if __name__ == '__main__':
    # print(answer_one())
    print(answer_two())
