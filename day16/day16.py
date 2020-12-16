#!/usr/bin/env python3
import re

from functools import reduce
from operator import mul

def parse_input(file):
    rules, ticket, nearby = dict(), [], []
    for line in open(file).readlines():
        rule = re.match(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', line)
        if rule:
            rules[rule.group(1)] = [
                (int(rule.group(2)), int(rule.group(3))), 
                (int(rule.group(4)), int(rule.group(5)))
                ]
            continue
        numbers = re.match(r'(\d+,?)+', line)
        if numbers and len(ticket) == 0:
            ticket = list(map(int, line.split(',')))
        elif numbers:
            nearby.append(list(map(int, line.split(','))))

    return rules, ticket, nearby


def is_invalid(rules, n):
    failed = []
    for r, intervals in rules.items():
        int_1, int_2 = intervals
        if not ((int_1[0] <= n <= int_1[1]) or (int_2[0] <= n <= int_2[1])):
            failed.append(r)
    return len(failed) == len(rules)


def possible_rules(rules, n):
    passed = set()
    for r, intervals in rules.items():
        int_1, int_2 = intervals
        if ((int_1[0] <= n <= int_1[1]) or (int_2[0] <= n <= int_2[1])):
            passed.add(r)
    return passed


def filter_valid_tickets(rules, tickets):
    valid_tickes = filter(lambda t: all(not is_invalid(rules, x) for x in t), tickets)
    return valid_tickes


def solve_part_1(rules, nearby):
    invalid = []
    for ticket in nearby:
        invalid += [t for t in ticket if is_invalid(rules, t)]
    return sum(invalid)


def solve_part_2(rules, nearby, ticket):
    valid_tickets = filter_valid_tickets(rules, nearby)
    rule_sets = [[possible_rules(rules, n) for n in t] for t in valid_tickets]
    intersections = [reduce(set.intersection, (r[j] for r in rule_sets)) for j in range(len(rule_sets[0]))]

    result = dict()
    while any(len(s) > 0 for s in intersections):
        sol = 0
        for i, s in enumerate(intersections):
            if len(s) == 1: sol = i
        result[sol] = intersections[sol]
        for i in range(len(intersections)):
            intersections[i] = intersections[i] - result[sol]
    
    wanted_fields = [i for i in result.keys() if result[i].pop().startswith('departure')]
    return reduce(mul, (ticket[f] for f in wanted_fields))


if __name__ == "__main__":
    rules, ticket, nearby = parse_input('input.txt')
    print(f'{solve_part_1(rules, nearby)}, {solve_part_2(rules, nearby, ticket)}')
