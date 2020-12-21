#!/usr/local/bin/python
import re


def answer_one():
    keyset = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    count = 0
    with open('2020_04_input.txt', 'r') as f:
        line = f.readline()
        last_line_linebreak = True
        tmp_keyset = None

        while line:
            line = line.rstrip()
            if last_line_linebreak:
                tmp_keyset = keyset.copy()

            if line:
                print(f'{line}')
                last_line_linebreak = False
                parts = line.split(' ')
                for part in parts:
                    key_value = part.split(':')
                    key = key_value[0]
                    if key in tmp_keyset:
                        tmp_keyset.remove(key)

            else:
                if len(tmp_keyset) == 0:
                    count += 1
                    print(f'VALID: {count}')
                last_line_linebreak = True
                print('-----')

            line = f.readline()
        if len(tmp_keyset) == 0:
            count += 1

    return count


def valid_height(x):
    if x[-2:] == 'in':
        return 59 <= int(x[:-2]) <= 76
    elif x[-2:] == 'cm':
        return 150 <= int(x[:-2]) <= 193
    else:
        return False


def answer_two():
    keyset = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': valid_height,
        'hcl': lambda x: True if re.match(r'^#[0-9a-f]{6}$', x) else False,
        'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda x: True if re.match(r'^\d{9}$', x) else False
    }
    count = 0
    with open('2020_04_input.txt', 'r') as f:
        line = f.readline()
        last_line_linebreak = True

        matches = 0
        while line:
            line = line.rstrip()
            if last_line_linebreak:
                matches = 0

            if line:
                print(f'{line}')
                last_line_linebreak = False
                parts = line.split(' ')
                for part in parts:
                    key_value = part.split(':')
                    key = key_value[0]
                    val = key_value[1]
                    if key in keyset:
                        print(f'{key}:{val}, is valid? {keyset[key](val)}')
                        if keyset[key](val):
                            matches += 1
                        else:
                            break

            else:
                print(f'matches: {matches} == keyset length: {len(keyset)}')
                if matches == len(keyset):
                    count += 1
                    print(f'VALID: {count}')
                last_line_linebreak = True
                print('-----')

            line = f.readline()
        if matches == len(keyset):
            count += 1

    return count


if __name__ == '__main__':
    # print(answer_one())
    print(answer_two())
