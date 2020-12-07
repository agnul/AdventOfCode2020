#!/usr/bin/env python3
import re

def parse_rules(lines):
    rules = dict()
    for l in lines:
        color, contains = l.split(' bags contain ')
        rules[color] = []
        if contains == 'no other bags.':
            continue
        bags = contains.split(', ')
        for b in bags:
            m = re.match(r'(\d+) ([a-z ]+) bags?', b)
            rules[color].append((int(m.group(1)), m.group(2)))
    return rules


def can_contain(bag, color, rules):
    bag_contents = [c for _, c in rules[bag]]
    if color in bag_contents or any(can_contain(c, color, rules) for c in bag_contents):
        return True
    return False


def count_bags_inside(color, bags):
    return 1 + sum(q * count_bags_inside(b, bags) for q, b in bags[color])


def solve_part_1b(rules):
    return len([b for b in rules.keys() if can_contain(b, 'shiny gold', rules)])


def solve_part_2(rules):
    return count_bags_inside('shiny gold', rules) - 1


if __name__ == "__main__":
    rules = parse_rules([l.rstrip() for l in open('input.txt').readlines()])
    print(f'{solve_part_1b(rules)}, {solve_part_2(rules)}')
