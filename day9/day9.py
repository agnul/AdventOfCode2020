#!/usr/bin/env python3
from itertools import combinations

def check_number(numbers, n):
    return any((a, b) for a, b in combinations(numbers, 2) if a != b and a + b == n)


def find_sum(numbers, s):
    for i in range(0, len(numbers)):
        for n in range(1, len(numbers) - i):
            if sum(numbers[i:i+n]) == s:
                return (i, n)
    return (-1, -1)


def solve_part_1(numbers, window_size):
    for i in range(0, len(numbers) - window_size):
        if not check_number(numbers[i:i + window_size], numbers[i + window_size]):
            return numbers[i + window_size]
    return -1


def solve_part_2(numbers, s):
    start, size = find_sum(numbers, s)
    return min(numbers[start:start+size]) + max(numbers[start:start+size])


if __name__ == "__main__":
    numbers = [int(l.rstrip()) for l in open('input.txt').readlines()]
    print(f'{solve_part_1(numbers, 25)}, {solve_part_2(numbers, 258585477)}')
