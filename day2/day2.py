#!/usr/bin/env python3
from functools import reduce

def parse(line):
    r, l, p = line.rstrip().split()
    min, max = map(int, r.split('-'))
    return ((min, max), l[0], p)


def inc(acc, _):
    return 1 + acc


def is_valid(entry):
    (min, max), c, p = entry
    count = reduce(inc, filter(lambda l: l == c, p), 0)
    return min <= count and count <= max


def is_valid_2(entry):
    (l, r), c, p = entry
    return (p[l - 1] == c) != (p[r - 1] == c)


def solve_part_1(input):
    return len([i for i in input if is_valid(i)])


def solve_part_2(input):
    return len([i for i in input if is_valid_2(i)])


if __name__ == "__main__":
    data = [parse(p) for p in open('input.txt').readlines()]
    print(f'{solve_part_1(data)}, {solve_part_2(data)}')
