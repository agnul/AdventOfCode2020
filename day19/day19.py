#!/usr/bin/env python3
import re

from collections import defaultdict

def parse_rule(s):
    return int(s) if str.isnumeric(s) else s[1:-1]


def parse(fname):
    rules, messages = dict(), []
    for ll in map(str.rstrip, open(fname).readlines()):
        if ': ' in ll:
            left, right = ll.replace('"', '').split(': ')
            rules[left] = right
        elif ll:
            messages.append(ll)
    return rules, messages


def expand(rules, r):
    if not r.isdigit():
        return r
    x = ''.join(map(lambda rr: expand(rules, rr), rules[r].split()))
    return f'(?:{x})'


def solve_part_1(rules, messages):
    rx = expand(rules, '0')
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
