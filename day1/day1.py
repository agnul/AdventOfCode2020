#!/usr/bin/env python3

data = sorted([int(m) for m in open('input.txt').read().split()])


def find_sum(numbers, target):
    if len(numbers) < 2 or numbers[0] + numbers[1] > target:
        return -1
    lo, hi = 0, len(numbers) - 1
    while lo != hi:
        if numbers[lo] + numbers[hi] < target:
            lo = lo + 1
        elif numbers[lo] + numbers[hi] == target:
            return numbers[lo] * numbers[hi]
        else:
            hi = hi - 1
    return -1


def solve_part_1(numbers):
    return find_sum(numbers, 2020)


def solve_part_2(numbers):
    for (i,n) in enumerate(numbers):
        if n > 2020:
            break
        p = find_sum(numbers[i + 1:], 2020 - n)
        if p != -1:
            return n * p
    return -1


if __name__ == "__main__":
    print(f'{solve_part_1(data)}, {solve_part_2(data)}')
