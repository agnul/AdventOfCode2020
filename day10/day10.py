#!/usr/bin/env python3
from collections import Counter

def paths_from(i, jolts, cache = dict()):
    if i == len(jolts) - 1: return 1

    if i in cache: return cache[i]

    p = 0
    for j in range(i + 1, min(i + 4, len(jolts))):
        if jolts[j] - jolts[i] <= 3:
            p += paths_from(j, jolts, cache)
    cache[i] = p
    return p


def solve_part_1(jolts):
    max_jolts = jolts[-1] + 3
    counts = Counter([b - a for a, b in zip([0] + jolts, jolts + [max_jolts])])
    return counts[1] * counts[3]


def solve_part_2(jolts):
    return paths_from(0, [0] + jolts + [jolts[-1] + 3])


if __name__ == "__main__":
    jolts = sorted([int(l.rstrip()) for l in open('input.txt').readlines()])
    print(f'{solve_part_1(jolts)}, {solve_part_2(jolts)}')
