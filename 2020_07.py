#!/usr/local/bin/python
from typing import Set, Dict, List
from unittest import TestCase
import re


def answer_one():
    # We build a map of sets of bags that contain colors so that we can
    # recursively look through the parent color relationships and count
    # each one

    child_bags: Dict[str, Set[str]] = {}
    with open('2020_07_input.txt', 'r') as f:
        line = f.readline()
        while line:
            parsed = get_bag_details(line.rstrip())
            parent_bag = parsed[0]
            for bag in parsed[1:]:
                color, count = bag
                children_of = child_bags.get(color, set())
                children_of.add(parent_bag)
                child_bags[color] = children_of

            line = f.readline()

    bags_counted = set()
    # for bag, parent_bags in child_bags.items():
    #     print(f'{bag} bags are in {parent_bags}')
    return count_unique_bags(child_bags, bags_counted, 'shiny gold')


def count_unique_bags(child_bags: Dict[str, Set[str]], bags_counted: Set[str], color: str):
    if color not in child_bags:
        return 0
    parent_colors = child_bags[color]
    count = 0
    for pc in parent_colors:
        if pc not in bags_counted:
            count += 1
            bags_counted.add(pc)
            count += count_unique_bags(child_bags, bags_counted, pc)
    return count


def answer_two():
    # This time we need to build a different map, one that lets us traverse the other direction
    # through the relationships and recursively calculate the total bags
    parent_bags: Dict[str, Dict[str, int]] = {}
    with open('2020_07_input.txt', 'r') as f:
        line = f.readline()
        while line:
            parsed = get_bag_details(line.rstrip())
            parent_color = parsed[0]
            for bag in parsed[1:]:
                color, count = bag
                parent_bag = parent_bags.get(parent_color, {})
                parent_bag[color] = count
                parent_bags[parent_color] = parent_bag

            line = f.readline()

    # for parent, child_bags in parent_bags.items():
    #     print(f'{parent} bags contain {child_bags}')
    bag_counts = []
    generate_bag_counts(parent_bags, bag_counts, 'shiny gold')
    count = 0
    for c in bag_counts:
        count += c
    return count


def generate_bag_counts(parent_bags: Dict[str, Dict[str, int]], bag_counts: List[int], color: str):
    if color not in parent_bags:
        return 1
    child_bags = parent_bags[color]
    print(f'{color} bags contain:')
    count = 0
    # TODO: Rewrite this - wrong calculation
    for child_color, child_count in child_bags.items():
        print(f' - {child_count} {child_color} bags')
        real_child_count = generate_bag_counts(parent_bags, bag_counts, child_color)
        count += child_count * real_child_count
    print(f' - {color} bags actually contain {count} bags')
    bag_counts.append(count)
    return count


def get_bag_details(line: str):
    words = line.split(' ')
    output = []
    index = 0

    current_word_list = []

    for word in words:
        if word[-1] in (',', '.'):
            word = word[:-1]
        if word in ('bag', 'bags'):
            index += 1
            if re.match(r'^\d+$', current_word_list[0]):
                output.append((' '.join(current_word_list[1:]), int(current_word_list[0])))
            else:
                if current_word_list == ['no', 'other']:
                    current_word_list = []
                    continue
                output.append(' '.join(current_word_list))
            current_word_list = []
            continue
        if word == 'contain':
            continue
        current_word_list.append(word)

    return output


if __name__ == '__main__':
    # print(answer_one())
    print(answer_two())


class TestStuff(TestCase):

    def test_get_bag_details(self):
        actual = get_bag_details(
            'dark orange bags contain 3 bright white bags, 4 muted yellow bags, 1 sample color bag.'
        )
        self.assertEqual(
            ['dark orange', ('bright white', 3), ('muted yellow', 4), ('sample color', 1)]
            , actual
        )

    def test_get_no_other_bags(self):
        actual = get_bag_details(
            'some color bags contain no other bags.'
        )
        self.assertEqual(
            ['some color']
            , actual
        )
