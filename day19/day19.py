#!/usr/bin/env python3
import re

from collections import defaultdict

def parse_rule(s):
    return int(s) if str.isnumeric(s) else s[1:-1]


def parse(fname):
    rules, messages = defaultdict(lambda: []), []
    for ll in map(str.rstrip, open(fname).readlines()):
        if ':' in ll:
            left, right = ll.split(':')
            rule = int(left)
            for s in right.split('|'):
                rules[rule].append([parse_rule(n) for n in s.split()])
        elif ll:
            messages.append(ll)
    return rules, messages


def build_rule(rules, r, part_2 = False):
    if isinstance(r, list) and isinstance(r[0], list) and len(r) > 1:
        return f'({"|".join(build_rule(rules, s) for s in r)})'
    elif isinstance(r, list):
        return f'{"".join(build_rule(rules, s) for s in r)}'
    elif isinstance(r, int):
        return build_rule(rules, rules[r])
    else:
        return r


def solve_part_1(rules, messages):
    rx = build_rule(rules, rules[0])
    count = 0
    for m in messages:
        if re.fullmatch(rx, m):
            count += 1
    return count


def solve_part_2(rules, messages):
    pass


if __name__ == "__main__":
    rules, messages = parse('input.txt')
    print(f'{solve_part_1(rules, messages)}, {solve_part_2(rules, messages)}')
