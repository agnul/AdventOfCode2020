#!/usr/bin/env python3
from functools import reduce
from itertools import count
from math import gcd, prod
from operator import mul, itemgetter

def solve_part_1(departure, buses):
    wait_times = [b - departure % b for _, b in buses]
    idx, min_wait = 0, wait_times[0]
    for b, w in enumerate(wait_times[1:], 1):
        if w < min_wait:
            idx, min_wait = b, w
    return buses[idx][1] * min_wait


def solve_part_2_slowly(buses):
    equations = sorted(buses, key=itemgetter(1), reverse=True)
    i, x = 1, equations[0][1]
    for r, n in equations[1:]:
        while x % n != n - r:
            x += reduce(mul, [a[1] for a in equations[:i]])
        i+=1
    return x


def solve_part_2(buses):
    n, step = 0, buses[0][1]
    for d, t in buses[1:]:
        for n in count(n, step):
            if (n + d) % t == 0:
                break
        step = (step * t) // gcd(step, t)
    return n


if __name__ == "__main__":
    lines = open('test.txt').readlines()
    departure, buses = int(lines[0]), []
    #for i, b in enumerate('67,x,7,59,61'.split(',')):
    for i, b in enumerate(lines[1].split(',')):
        if b != 'x': buses.append((i, int(b)))
    print(f'{solve_part_1(departure, buses)}, {solve_part_2(buses)}')
