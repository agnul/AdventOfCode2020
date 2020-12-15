#!/usr/bin/env python3
from collections import defaultdict, deque
from functools import reduce
from operator import sub

def play(numbers, rounds):
    said_at, last_spoken_at = dict(), defaultdict(lambda: deque([], 2))
    for i, n in enumerate(numbers):
        said_at[i + 1] = n
        last_spoken_at[n].appendleft(i + 1)
    for t in range(len(numbers) + 1, rounds + 1):
        prev, say = said_at[t - 1], 0
        if len(last_spoken_at[prev]) == 2:
            say = reduce(sub, last_spoken_at[prev])
        said_at[t] = say
        last_spoken_at[say].appendleft(t)
    return said_at[rounds]


def solve_part_1(numbers):
    return play(numbers, 2020)


def solve_part_2(numbers):
    return play(numbers, 30000000)


if __name__ == "__main__":
    print(f'{solve_part_1([19,0,5,1,10,13])}, {solve_part_2([19,0,5,1,10,13])}')
