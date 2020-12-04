#!/usr/bin/env python3
from functools import reduce


def solve_part_1(tree_map, right, down):
    c, r = 0, right
    for line in tree_map[down::down]:
        if line[r] == '#':
            c += 1
        r = (r + right) % len(line)
    return c


def solve_part_2(tree_map):
    counts = [solve_part_1(tree_map, r, d) for (r, d) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
    return reduce(lambda x, y: x * y, counts)

if __name__ == "__main__":
    trees = [line.rstrip() for line in open('input.txt').readlines()]
    print(f'{solve_part_1(trees, 3, 1)}, {solve_part_2(trees)}')
